from PySide2.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QSizePolicy, QComboBox
from functools import partial
from PySide2.QtCore import Qt
from charts.mpl_widget import MplWidget
from charts.chart import Bar_chart_edge_numbers
from charts.chart_one_node import Chart_one_node
from charts.chart_number_of_edge_of_node import Chart_number_of_edge_of_node
from charts.chart_sum_of_edge_prop_of_one_node import Chart_sum_of_edge_prop_of_one_node
from charts.chart_compare import Chart_compare
from graph_data.result_run import Result_run


class Statistics_menu_window(QWidget):

    def __init__(self, parent):

        self.mapping = {'A gráfok rajzolása.': MplWidget,
                   'Élek súlyának megtekintése.': Bar_chart_edge_numbers,
                    "Egy adott csomópont éleinek megtekíntése.": Chart_one_node,
                    "A csomópontok éleinek száma.": Chart_number_of_edge_of_node,
                    "A csomopontok éleinek össz súlyértéke.": Chart_sum_of_edge_prop_of_one_node,
                    "Összehasonlítás, egyező élek szerint.": Chart_compare
                   }

        for name, class_type in self.mapping.items():
            class_type.class_name = name

        QWidget.__init__(self)
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.parent = parent
        self.add_parameters_window = None
        self.label = QLabel(self)
        self.label.setText("Statiszika megjelenítésének formája:")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label.setStyleSheet("font: 15pt")
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        layout.addWidget(self.label)
        self.buttons = []

        self.label1 = QLabel(self)
        self.label1.setText('Gráf neve:')
        layout.addWidget(self.label1)

        self.combo_box = QComboBox(self)

        if Result_run.getInstance().run_property is not None:
            # self.combo_box.addItems(Result_run.getInstance().run_property.unique_property)
            self.add_prop_to_combobox(Result_run.getInstance().run_property.unique_property)

        layout.addWidget(self.combo_box)

        for key, value in self.mapping.items():
            self.buttons.append(QPushButton(key, self))
            self.buttons[-1].clicked.connect(partial(self.handleButton, chart_class=value))
            layout.addWidget(self.buttons[-1])
        self.worker_thread = None

        self.prop_name = None

        # self.combo_box.currentIndexChanged.connect(
        #     partial(selection_change,
        #             widget=widget,
        #             parameter_names=parameter_names,
        #             controller_function=controller_function)
        # )
        #
    # def selection_change

    def add_prop_to_combobox(self, prop_list):
        self.combo_box.clear()
        self.combo_box.addItems(prop_list)

    def show(self) -> None:
        super(Statistics_menu_window, self).show()
        if Result_run.getInstance().run_property is not None:
            # self.combo_box.addItems(Result_run.getInstance().run_property.unique_property)
            self.add_prop_to_combobox(Result_run.getInstance().run_property.unique_property)

    # elinditja a statisztikat
    def handleButton(self, chart_class="\n"):

        result_list = self.parent.result_run.result
        live_data = self.parent.statistics_live_data
        live_data.property_name = self.combo_box.currentText()
        live_data.data = chart_class

        self.hide()










