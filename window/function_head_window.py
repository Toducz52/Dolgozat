from PySide2.QtWidgets import QWidget
from window.ui_py.ui_function_head_window import Ui_Form
from PySide2.QtCore import Slot, SIGNAL, QObject
from util.util_regex import is_valid_function_name
from util.util_msg_box import create_simple_message_box_and_run


class Function_head_detail:

    def __init__(self, function_name, arg_list):
        self.function_name = function_name
        if type(arg_list) is list:
            self.args = {i: '' for i in arg_list}
        else:
            self.args = arg_list


class Function_head_window(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.function_head = ''
        self.function_head_detail = None
        QObject.connect(self.ui.btn_add_parameter, SIGNAL("clicked()"), self.add_parameter)
        QObject.connect(self.ui.btn_delete_parameter, SIGNAL("clicked()"), self.delete_parameter)
        QObject.connect(self.ui.btn_create_function_head, SIGNAL("clicked()"), self.create_function_head)
        self.ui.btn_back.clicked.connect(self.back)

    def load_data(self, function_head_detail):
        self.ui.in_function_name.setText(function_head_detail.function_name)
        self.ui.list_parameter.clear()
        self.ui.list_parameter.addItems(function_head_detail.args.keys())
        self.function_head_detail = function_head_detail
        self.parent.ui.in_code.code_text_change_is_available()


    def back(self):
        self.hide()

    def create_function_head(self):

        function_name = self.ui.in_function_name.text()
        parameter_list = []
        for index in range(0, self.ui.list_parameter.count()):
            parameter_list.append(self.ui.list_parameter.item(index).text())

        error = ''

        if not is_valid_function_name(function_name):
            error = 'A függvénynév helytelen vagy nem létezik\n'

        if self.ui.list_parameter.count() == 0:
            error = error + "A paraméterlista nem lehet üress! Legalább egy parametert kell tartalmazzon.\n"

        if error == '':
            self.parent.ui.in_code.code_text_change_is_available()
            self.function_head = self.parent.ui.in_code.add_function_head_to_code(function_name, parameter_list)
            self.function_head_detail = Function_head_detail(function_name, parameter_list)
        else:
            create_simple_message_box_and_run(self, error)

        self.hide()

    @Slot()
    def add_parameter(self):

        parameter = self.ui.in_parameter.text()

        error = ""

        if not is_valid_function_name(parameter):
            error = 'A paraméter helytelen.\n'

        for index in range(0, self.ui.list_parameter.count()):
            item = self.ui.list_parameter.item(index)
            if item.text() == parameter:
                error = 'A paraméter már létezik.'

        if error == "":
            self.ui.list_parameter.addItem(parameter)
        else:
            create_simple_message_box_and_run(self, error)

    @Slot()
    def delete_parameter(self):

        list_selected_item = self.ui.list_parameter.selectedItems()

        for item in self.ui.list_parameter.selectedItems():
            self.ui.list_parameter.takeItem(self.ui.list_parameter.row(item))
