from db.DB import *


class DB_query:

    dao = DAO(DB)
    repo = Repository(dao)

    @classmethod
    def can_be_changed_algorithm(cls, save_name):

        result = cls.repo.get_build_in_name(save_name)

        if result.success:
            if len(result.value) > 0:
                return False
            else:
                return True
        else:
            raise result.error


if __name__ == '__main__':

    db = DB_query()

    if db.can_be_changed_algorithm('kerlek'):
        print("Changed")
    else:
        print("not changed")

