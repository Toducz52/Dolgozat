import sqlite3
from model.algorithm_wrapper import *
from util.util_result import Result
import os
from datetime import datetime


class DB_exception(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(DB_exception, self).__init__(message)


class DB(object):

    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if DB._instance is None:

            DB._instance = cls.__new__(cls)

            try:
                DB._instance.connect = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'example.db'))
                DB._instance.cursor = DB._instance.connect.cursor()
            except Exception as db_error:
                raise DB_exception(str(db_error))
        return cls._instance

    # def __del__(self):
    #     if self._instance is not None:
    #         self._instance.connect.close()
    #         self._instance.cursor.close()


class IDao:

    def __init__(self, db: DB):
        try:
            self.db = db.instance()
        except Exception as db_error:
            print(db_error)

    def add_algorithm(self, algorithm_wrapper: Algorithm_wrapper) -> Result:
        pass

    def get_algorithm_base_save_name(self, save_name) -> Result:
        pass

    def get_save_names(self) -> Result:
        pass

    def get_build_in_names(self, save_name) -> Result:
        pass

    def delete_algorithm(self, save_name) -> Result:
        pass

    def update_algorithm(self, save_name) -> Result:
        pass

def factory_algorithm_wrapper(result, function_call, args) -> Algorithm_wrapper:
    save_name = result[0]
    function_name = result[1]
    create_date = result[2]
    update_date = result[3]
    readme = result[4]
    code = result[5]
    return Algorithm_wrapper().initialization(save_name, function_name, readme, code, function_call, args, create_date,
                                              update_date)


def p(text):
    return f"\'{text}\'"

def code_add_quote(code):

  text = ''

  for c in code:
    # print(c)
    # print('-->' + '\'')
    if c == "'":
      text += "'"
    text += c
  return text

class DAO(IDao):

    def __init__(self, db: DB):
        super().__init__(db)

    def add_algorithm(self, alg_wrapper: Algorithm_wrapper) -> Result:

        for parameter in alg_wrapper.args.keys():
            query = f'''INSERT INTO parameters VALUES("{alg_wrapper.save_name}", "{parameter}")'''

            try:
                self.db._instance.cursor.execute(query)
            except Exception as error:
                self.db._instance.connect.rollback()
                return Result.Fail(error)

        code = code_add_quote(alg_wrapper.code)

        insert = f'''INSERT INTO algorithms (save_name,function_name,create_date,update_date,readme, code) VALUES('{alg_wrapper.save_name}', '{alg_wrapper.function_name}', '{alg_wrapper.create_date}', '{datetime.today().strftime('%Y-%m-%d-%H:%M')}', '{alg_wrapper.readme}', '{code}')'''
        # query = insert.format(p(), p(), p(), p(), p(), p())
        query = insert


        try:
            # print(query)
            self.db._instance.cursor.execute(query)
        except Exception as error:
            self.db._instance.connect.rollback()
            return Result.Fail(error)

        for call in alg_wrapper.function_call:
            query = f'''INSERT INTO function_call VALUES('{alg_wrapper.save_name}', '{call.v1}', '{call.v2}', '{call.prop}', '{call.start}', '{call.end}')'''
            try:
                self.db._instance.cursor.execute(query)
            except Exception as error:
                self.db._instance.connect.rollback()
                return Result.Fail(error)

        self.db._instance.connect.commit()
        return Result.Ok()

    def get_algorithm_base_save_name(self, save_name) -> Result:

        function_call = []

        try:
            query = f'''SELECT * FROM algorithms WHERE algorithms.save_name == "{save_name}" LIMIT 1'''
            self.db._instance.cursor.execute(query)
            result_algorithm = self.db._instance.cursor.fetchone()

            query = f'''SELECT * FROM function_call WHERE function_call.save_name == "{save_name}"'''
            self.db._instance.cursor.execute(query)
            result_function_call = self.db._instance.cursor.fetchall()

            for call in result_function_call:
                function_call.append(Function_call(call[1], call[2], call[3], call[4], call[5]))

            query = f'''SELECT * FROM parameters WHERE parameters.save_name == "{save_name}"'''
            self.db._instance.cursor.execute(query)
            result_parameters = self.db._instance.cursor.fetchall()
            res_dct = {i[1]: '' for i in result_parameters}

            algorithm = factory_algorithm_wrapper(result_algorithm, function_call, res_dct)

            return Result.Ok(algorithm)

        except sqlite3.Error as error:
            return Result.Fail(error)

    def get_save_names(self) -> Result:
        try:
            query = '''SELECT save_name FROM algorithms'''
            self.db._instance.cursor.execute(query)
            result = self.db._instance.cursor.fetchall()
            return Result.Ok(result)
        except sqlite3.Error as error:
            return Result.Fail(error)

    def get_build_in_name(self, save_name) -> Result:
        try:
            query = f'''SELECT save_name FROM build_in_algorithms WHERE save_name = "{save_name}"'''
            self.db._instance.cursor.execute(query)
            result = self.db._instance.cursor.fetchall()
            return Result.Ok(result)
        except sqlite3.Error as error:
            return Result.Fail(error)

    def delete_algorithm(self, save_name) -> Result:
        try:
            query1 = f'''DELETE FROM parameters WHERE save_name = "{save_name}"'''
            query2 = f'''DELETE FROM algorithms WHERE save_name = "{save_name}"'''
            query3 = f'''DELETE FROM function_call WHERE save_name = "{save_name}"'''

            self.db._instance.cursor.execute(query1)
            self.db._instance.cursor.execute(query2)
            self.db._instance.cursor.execute(query3)

            self.db._instance.connect.commit()
            return Result.Ok(True)
        except sqlite3.Error as error:
            return Result.Fail(error)

    def update_algorithm(self, alg: Algorithm_wrapper) -> Result:

        try:
            self.delete_algorithm(alg.save_name)
            self.add_algorithm(alg)
            return Result.Ok(True)
        except Exception as error:
            raise Result.Fail(error)


class Repository:

    def __init__(self, dao: IDao):
        self.dao = dao

    def add_algorithm(self, algorithm_wrapper: Algorithm_wrapper) -> bool:
        return self.dao.add_algorithm(algorithm_wrapper)

    def get_algorithm_base_save_name(self, save_name) -> Result:
        return self.dao.get_algorithm_base_save_name(save_name)

    def get_save_names(self):
        return self.dao.get_save_names()

    def get_build_in_name(self, save_name):
        return self.dao.get_build_in_name(save_name)

    def delete_algorithm(self, save_name):
        return self.dao.delete_algorithm(save_name)

    def update_algorithm(self, alg: Algorithm_wrapper):
        return self.dao.update_algorithm(alg)


if __name__ == '__main__':

    dao = DAO(DB)
    repo = Repository(dao)
    #
    # alg = Algorithm_wrapper()
    # alg.args = {'b': 4}
    # alg.code = "code"
    # alg.function_name = "Koszonom"
    #
    wrapper = repo.get_algorithm_base_save_name("koszonom_endi")
    if wrapper.success:
        print(wrapper.value)

    wrapper.value.save_name = 'Endi'

    result = None

    try:
        result = repo.add_algorithm(wrapper.value)
    except Exception as error:
        print("ASd")
        print(error)

    # print(str(result))



    # db = DB.instance()
    # cur = db._instance.cursor.execute("SELECT * FROM algorithms")
    # # cur.execute("SELECT * FROM algorithms")
    # records = db._instance.cursor.fetchall()
    # print(str(records))

    # if a is None:
    #     print("alma")
    # else:
    #     try:
    #         a.exec('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')
    #     except Exception as error:
    #         print(error)
    #
    #     try:
    #         a.exec('''INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)''')
    #     except Exception as error:
    #         print(error)
    #
    #     try:
    #         a.exec('''INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)''')
    #     except Exception as error:
    #         print(error)
    #
    #
    #     # t = ('RHAT',)
    #     # a.cursor.execute('SELECT * FROM stocks WHERE symbol=?', t)
    #     # # print(a.cursor.fetchone())
