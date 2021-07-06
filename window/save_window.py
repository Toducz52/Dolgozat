from PySide2.QtWidgets import QWidget
from window.ui_py.ui_save_window import Ui_Form
from util.util_msg_box import create_simple_message_box_and_run
from model.algorithm_wrapper import Algorithm_wrapper
from util.util_db_query import DB_query


class Save_window(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.btn_save.clicked.connect(self.save_as)
        self.ui.btn_back.clicked.connect(self.back)

    def back(self):
        self.hide()

    def get_data(self):
        code = self.parent.ui.in_code.toPlainText()

        save_name = self.ui.in_save_name.text()
        function_head_detail = self.parent.function_head_window.function_head_detail
        if function_head_detail is None:
            raise Exception("Függvénynév nincs inicializálva.")
        readme = self.ui.in_readme.toPlainText()

        try:
            function_calls = self.parent.create_edge_window.get_list_of_active_function_call()
        except Exception as ex:
            raise ex

        return save_name, function_head_detail, code, function_calls, readme

    def save_as(self):

        try:
            save_name, function_head_detail, code, function_calls, readme = self.get_data()

            # result = self.parent.repo.get_build_in_name(save_name)
            #
            # if result.success:
            #     if len(result.value) > 0:
            #         create_simple_message_box_and_run(self, "Nem lehet modositani ezt a mentest.")
            #         return None
            # else:
            #     create_simple_message_box_and_run(self, "Váratlan hiba történt.")
            #     return None

            algorithm = Algorithm_wrapper().initialization(save_name, function_head_detail.function_name, readme, code,
                                                           function_calls, function_head_detail.args)
            result = self.parent.repo.add_algorithm(algorithm)

            self.parent.session_name = algorithm.save_name
            self.parent.ui.out_session_name.setText(self.parent.session_name)


            if result.failure:
                if 'UNIQUE constraint' in str(result.error):
                    create_simple_message_box_and_run(self, "Ezzel a névvel már történt mentés.")
                else:
                    create_simple_message_box_and_run(self, "Váratlan hiba történt1.")
            else:
                create_simple_message_box_and_run(self, "A mentés sikeresen megtörtént.")

        except Exception as ex:
            create_simple_message_box_and_run(self, str(ex))

    def save(self):

        try:
            save_name, function_head_detail, code, function_calls, readme = self.get_data()

            # mert itt mar biztos kell legyen benne
            save_name = self.parent.session_name

            if DB_query.can_be_changed_algorithm(save_name):

            # result = self.parent.repo.get_build_in_name(save_name)
            #
            # if result.success:
            #     if len(result.value) > 0:
            #         create_simple_message_box_and_run(self, "Nem lehet modositani ezt a mentest.")
            #         return None
            # else:
            #     create_simple_message_box_and_run(self, "Váratlan hiba történt.")
            #     return None

                create_date = self.parent.load_alg_wrapper.create_date

                algorithm = Algorithm_wrapper().initialization(save_name, function_head_detail.function_name, readme, code,
                                                               function_calls, function_head_detail.args, create_date)

                result = self.parent.repo.update_algorithm(algorithm)

                # update
                if result.failure:
                    create_simple_message_box_and_run(self, "Váratlan hiba történt.")
                    return None
                else:
                    create_simple_message_box_and_run(self, "A mentés sikeresen megtörtént.")
                    return True
            else:
                create_simple_message_box_and_run(self, "Ez a munkamenet be van ágyazva nem lehet modosítani.")

        except Exception as ex:
            create_simple_message_box_and_run(self, str(ex))
            return None







