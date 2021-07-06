from graph_data.result_run import Result_run
from PySide2.QtWidgets import QWidget
from window.ui_py.ui_static_view import Ui_Form


class Statistics_view(QWidget):

    def page_rotate_next(self):

        self.page_number += 1

        if self.page_number >= self.all_page_number:
            self.page_number = 0

        self.page_update()

    def page_rotate_prev(self):

        self.page_number -= 1

        if self.page_number < 0:
            self.page_number = self.all_page_number

        self.page_update()

    def page_update(self):

        print(self.page_number)

        for row in range(0, 2):
            for column in range(0, 3):
                # current_widget_index = self.page_number * 6 + (row + 1) * (1 if row > 0 and column == 0 else column + 1)
                current_widget_index = self.page_number * 6 + row * 3 + column

                if current_widget_index == len(self.graph_list):
                    return None

                widget = self.ui.gridLayout.itemAtPosition(row, column).widget()

                #print(inspect.getmembers(self.mode_class, predicate=inspect.isfunction))

                # inspect.signature(widget)
                self.current_index = current_widget_index
                widget.final(self.graph_list[current_widget_index])



                # print(str(row) + ":" + str(column) + ":" + f"{current_widget_index}")

                # self.ui.gridLayout.addWidget(self.widget_list[current_widget_index], row, column)

    def __init__(self, parent):

        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.current_index = 0

        self.parent = parent

        self.page_number = 0

        self.mode_class = self.parent.statistics_live_data.data

        run_result = Result_run.getInstance()

        self.run_property = run_result.run_property
        self.graph_list = run_result.result

        number_of_graph = len(self.graph_list)

        self.all_page_number = number_of_graph // 6

        for row in range(0, 2):
            for column in range(0, 3):
                widget = self.mode_class(self, self.run_property)
                # print(inspect.getmembers(self.mode_class, predicate=inspect.isfunction))
                self.ui.gridLayout.addWidget(widget, row, column)

        self.page_update()

        if number_of_graph > 6:
            self.ui.btn_next.clicked.connect(self.page_rotate_next)
            self.ui.btn_back.clicked.connect(self.page_rotate_prev)
        else:
            self.ui.btn_next.hide()
            self.ui.btn_back.hide()

        self.ui.btn_exit.clicked.connect(self.exit)

        self.ui.out_set_mode.setText('A elemzési módszer: ' + self.mode_class.class_name)
        self.ui.out_set_graph_name.setText('Gráf neve, amelyet elemez: ' + self.parent.statistics_live_data.property_name)

    def exit(self):
        self.hide()





