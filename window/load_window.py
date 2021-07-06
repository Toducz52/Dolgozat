from PySide2.QtWidgets import QWidget
from window.ui_py.ui_load_window import Ui_Form
from PySide2.QtCore import Slot, SIGNAL, QObject
from util.util_msg_box import create_simple_message_box_and_run
from model.algorithm_wrapper import Algorithm_wrapper
from window.function_head_window import Function_head_detail


class Load_window(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.btn_back.clicked.connect(self.back)
        self.initialization()
        QObject.connect(self.ui.listWidget, SIGNAL("itemSelectionChanged()"), self.selection_changed)
        self.ui.btn_delete.clicked.connect(self.delete)
        self.ui.btn_load.clicked.connect(self.load)

    @Slot()
    def load(self):

        selected_algorithm = self.selected_element()
        if selected_algorithm.failure:
            create_simple_message_box_and_run(self, "Nem lehet betölteni. Hiba történt.")
            return None

        alg = selected_algorithm.value

        self.parent.ui.in_code.signal_not_work = True
        self.parent.ui.in_code.setPlainText(alg.code)
        self.parent.ui.in_code.signal_not_work = False

        self.parent.ui.in_code.prev_text = self.parent.ui.in_code.toPlainText()
        self.parent.ui.in_code.prev_text_size = len(self.parent.ui.in_code.toPlainText())
        self.parent.function_head_window.load_data(Function_head_detail(alg.function_name, alg.args))
        self.parent.create_edge_window.load_data(alg.function_call)
        list_ = list(alg.args.keys())
        self.parent.ui.in_code.add_function_head_to_code(alg.function_name, list_)

        self.parent.ui.in_code.load_cannot_be_edited_interval(alg.function_call)

        self.parent.session_name = alg.save_name
        self.parent.ui.out_session_name.setText(alg.save_name)
        self.parent.load_alg_wrapper = alg

    @Slot()
    def delete(self):

        selected_item = self.ui.listWidget.selectedItems()
        if len(selected_item) > 1:
            create_simple_message_box_and_run(self, "Csak egyet valasszon ki.")
            return None

        save_name = selected_item[0].text()

        result = self.parent.repo.get_build_in_name(save_name)

        if result.success:
            if len(result.value) > 0:
                create_simple_message_box_and_run(self, "Nem lehet törölni.")
                return None
        else:
            create_simple_message_box_and_run(self, "Váratlan hiba történt.")
            return None

        result = self.parent.repo.delete_algorithm(save_name)

        if result.success:
            create_simple_message_box_and_run(self, "A törlés sikeres volt.")
        else:
            print("Valami hiba történt.")

        self.initialization()

    def selected_element(self):
        selected_item = self.ui.listWidget.selectedItems()

        if len(selected_item) == 0:
            return None

        if len(selected_item) > 1:
            create_simple_message_box_and_run(self, "Csak egyet valasszon ki.")
            return None

        save_name = selected_item[0].text()

        result = self.parent.repo.get_algorithm_base_save_name(save_name)

        return result

    @Slot()
    def selection_changed(self):

        result = self.selected_element()

        if result and result.success:
            algorithm_wrapper: Algorithm_wrapper = result.value
            self.ui.out_save_name.setText(algorithm_wrapper.save_name)
            self.ui.out_readme.setText(algorithm_wrapper.readme)
            self.ui.out_create_date.setText(algorithm_wrapper.create_date)
            self.ui.out_update_date.setText(algorithm_wrapper.update_date)
            self.ui.out_function_name.setText(algorithm_wrapper.function_name)


    @Slot()
    def back(self):
        self.hide()

    def initialization(self):
        result = self.parent.repo.get_save_names()
        if result.success:
            save_names = [i[0] for i in result.value]
            self.ui.listWidget.clear()
            self.ui.out_readme.clear()
            self.ui.listWidget.addItems(save_names)
        else:
            create_simple_message_box_and_run(self, "Váratlan hiba történt.")

