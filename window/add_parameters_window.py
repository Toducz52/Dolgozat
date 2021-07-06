
from worker_thread import WorkerThread
from builder_method.build_algorithm import build_algorithm_method
from PySide2.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout, QVBoxLayout, QLabel, QLineEdit, \
    QComboBox, QSizePolicy
from runner.runner_algorithm import Runner_algorithm
from PySide2.QtCore import Qt
import sys
from functools import partial
from util.util_msg_box import *
from model.algorithm_wrapper import *
from graph_data.run_property import Run_property
from graph_data.result_run import Result_run


def grid_real_row_count(grid):
    number_of_widget = grid

    if grid.columnCount() == 0:
        return 0

    row_count = int(grid.count() / 2)

    return row_count


def add_input_value_element_to_form(widget, parameter_names, controller_function=None):
    grid = widget.layout()

    label2 = QLabel("Paraméterek", widget)
    label2.setStyleSheet("font: 10pt")
    grid.addWidget(label2, grid_real_row_count(grid), 0)

    label3 = QLabel(":", widget)
    label3.setStyleSheet("font: 10pt")
    grid.addWidget(label3, grid_real_row_count(grid), 1)

    column_size = grid_real_row_count(grid)

    # print('value' + str(column_size))
    for name, index in zip(parameter_names, range(column_size, column_size + len(parameter_names), 1)):
        label = QLabel(name, widget)
        grid.addWidget(label, index, 0)
        lineEdit = QLineEdit(widget)
        grid.addWidget(lineEdit, index, 1)


def add_input_array_element_to_form(widget, parameter_names, controller_function=None):
    grid = widget.layout()

    label = QLabel("Tömb", widget)
    grid.addWidget(label, grid_real_row_count(grid), 0)

    comboBox = widget.comboBox
    comboBox.show()
    comboBox.addItems(parameter_names)
    grid.addWidget(comboBox, grid_real_row_count(grid), 1)

    label1 = QLabel("Tömb mérete", widget)
    grid.addWidget(label1, grid_real_row_count(grid), 0)

    lineEdit = QLineEdit("5", widget)
    grid.addWidget(lineEdit, grid_real_row_count(grid), 1)

    comboBox.currentIndexChanged.connect(
        partial(selection_change,
                widget=widget,
                parameter_names=parameter_names,
                controller_function=controller_function)
    )

    add_input_value_element_to_form(widget, parameter_names[1:])


def create_draw_color_form(widget, parameter_names, controller_function=None):
    grid = widget.layout()

    label1 = QLabel("Hány színnel legyen kiszinezve -->", widget)
    grid.addWidget(label1, grid_real_row_count(grid), 0)

    lineEdit = QLineEdit("5", widget)
    grid.addWidget(lineEdit, grid_real_row_count(grid), 1)

    label1 = QLabel("Válasszon ki egy gráfot!", widget)
    grid.addWidget(label1, grid_real_row_count(grid), 0)

    run_property = Result_run.getInstance().run_property
    prop_list = []
    if run_property is not None:
        prop_list = run_property.unique_property
    comboBox = QComboBox(widget)
    comboBox.addItems(prop_list)
    grid.addWidget(comboBox, grid_real_row_count(grid), 1)

    # add_input_array_element_to_form(widget, parameter_names, controller_function)


def selection_change(index, widget=None, parameter_names=None, controller_function=None):
    grid = widget.layout()

    list = parameter_names[:]

    jump_row = 6
    if controller_function == 'run_drawing_with_colors':
        jump_row = 8

    while True:
        item = grid.takeAt(jump_row)
        # print('*** --> ' + str(grid_real_row_count(grid)))
        if item:
            item.widget().hide()
            # print(item)
            # print('--' + str(grid.count()) + '--')
            del item
        else:
            break

    del list[index]

    add_input_value_element_to_form(widget, list)

    # print(str(grid.columnCount()) + '--> columnCount')
    # print(str(grid.count()) + '--> count')
    # print(str(grid.rowCount()) + '-->rowCount')

    # for index in range(grid.rowCount()):
    #     widget = grid.itemAtPosition(index, 1)
    #     if widget:
    #         if widget.widget():
    #             print(str(index) + '-->' + str(widget.widget()))
    #         else:
    #             print(str(index) + '-->' + 'None widget in layoutItem')
    #     else:
    #         print(str(index) + '-->' + 'None')

    # grid.update()
    # widget.update()


mapping = {
    'run_simple': add_input_value_element_to_form,
    'run_all_permutation': add_input_array_element_to_form,
    'run_all_permutation_sum': add_input_array_element_to_form,
    'run_random_array': add_input_array_element_to_form,
    'run_drawing_with_colors': create_draw_color_form
}


class Add_parameters_window(QWidget):

    def __init__(self, parent, func):
        super().__init__()

        self.parent = parent

        self.run_property = Result_run.getInstance().run_property

        if self.parent.parent.function_head_window.function_head_detail is None:
            raise Exception("Nincs beállítva a fejléc.")
        else:
            self.args = self.parent.parent.function_head_window.function_head_detail.args
        # print(self.args)

        self.controller_function = func
        self.controller_class = Runner_algorithm()

        self.setUi()

        self.worker_thread = None

        # Result_run.getInstance().get_signal_error().connect(self.error_handle)

    def error_handle(self, error):
        print(error)

    def setUi(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.label = QLabel(self)
        self.label.setText("Paraméterek megadása")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.label.setStyleSheet("font: 15pt")
        layout.addWidget(self.label)


        widget = QWidget(self)
        grid = QGridLayout(widget)

        label2 = QLabel("Specifikáció", widget)
        label2.setStyleSheet("font: 10pt")
        grid.addWidget(label2, grid_real_row_count(grid), 0)

        label3 = QLabel(":", widget)
        label3.setStyleSheet("font: 10pt")
        grid.addWidget(label3, grid_real_row_count(grid), 1)

        widget.setLayout(grid)
        self.layout().addWidget(widget)
        widget.comboBox = QComboBox(widget)
        widget.comboBox.hide()
        self.gridWidget = widget

        parameter_names = list(self.args.keys())
        mapping[self.controller_function](widget, parameter_names, self.controller_function)
        # self.add_form_element_parameter_in(widget, grid, names)

        self.btn_run = QPushButton("Futtat", self)
        self.layout().addWidget(self.btn_run)
        self.btn_run.clicked.connect(self.run)

    def run(self):
        try:
            self.get_data()
            alg: Algorithm_wrapper = self.parent.parent.create_algorithm_wrapper()
        except ValueError as error:
            create_detail_message_box(self, str(error), "Megnem fogalmazott leiras")
            return None

        alg.args = self.run_property.args
        self.run_property.alg = alg
        self.run_property.unique_property = self.parent.parent.create_edge_window.get_list_unique_prop()


        build_result = build_algorithm_method(self.run_property.alg)

        if build_result.success:


            self.worker_thread = WorkerThread(
                    self,
                    self.controller_function,
                    self.run_property,
                    Result_run.getInstance()
                )

            self.worker_thread.start()

            # if self.worker_thread.error is not None:
            #     create_detail_message_box(self.parent.parent, "Hiba történt", self.worker_thread.error)
            # else:
            #     self.parent.hide()
            #     self.hide()
            # print(self.worker_thread.error)

        else:
            create_simple_message_box_and_run(self, str(build_result.error))

        print("Futtat")
        self.hide()
        self.parent.hide()

        # run_result = Result_run.getInstance()
        #
        # print(len(run_result.result))
        #
        # print(run_result)

    def set_get_array_and_size_name(self, location):
        array_name = self.gridWidget.layout().itemAtPosition(location, 1).widget().currentText()
        array_size = self.gridWidget.layout().itemAtPosition(location + 1, 1).widget().text()
        if not array_size.isnumeric():
            raise ValueError(f"Kérem érvényes számot adjon meg a tömb méretéhez!")
        self.run_property.array_size = array_size
        self.run_property.array_name = array_name

    def get_data(self):

        if self.controller_function == 'run_drawing_with_colors':
            label_name = self.gridWidget.layout().itemAtPosition(1, 1).widget().text()
            if not label_name.isnumeric():
                raise ValueError(f"{label_name} nem szám. Kérem számot adjon meg!")
            self.run_property.color_number = int(label_name)

            graph_name = self.gridWidget.layout().itemAtPosition(2, 1).widget().currentText()
            if graph_name is None:
                raise Exception("Nincsen kiválasztható gráf.")
            self.run_property.graph_name = graph_name
            return None

        if self.run_property:
            del self.run_property

        self.run_property = Run_property()

        start = grid_real_row_count(self.gridWidget.layout()) - len(self.args)
        end = grid_real_row_count(self.gridWidget.layout())

        if not self.controller_function == 'run_simple':
            self.set_get_array_and_size_name(1)
            start += 1

        args = {}

        for index in range(start, end):
            label_name = self.gridWidget.layout().itemAtPosition(index, 0).widget().text()
            value = self.gridWidget.layout().itemAtPosition(index, 1).widget().text()

            if not check_parameter_value(value):
                raise ValueError(f"{label_name} parameter nem megfelelő!")

            try:
                args[label_name] = eval(f'{value}')
            except Exception as error:
                raise ValueError(f"{label_name} parameter nem megfelelő!")

        # print(args)
        self.run_property.args = args


def check_parameter_value(value):
    if value == "":
        return False
    return True


if __name__ == "__main__":
    app = QApplication([])
    widget = Add_parameters_window(None)
    widget.setWindowTitle("Test")
    widget.show()
    sys.exit(app.exec_())
