import sys
from PySide2.QtCore import QPoint, Qt, QCoreApplication
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QComboBox
from PySide2.QtCharts import QtCharts
from charts.chart_interface import  Chart_abstract
import copy
from charts.mpl_widget import arrayToString


class Chart_one_node(Chart_abstract):

    def draw_(self, widget):
        graph = self.result_graph.graph

        prop = self.prop

        current_text = self.combo_box.currentText()
        # default = int(current_text) if current_text else None

        default = None

        if current_text is not None:
            try:
                default = int(current_text)
            except:
                default = current_text

        edge_list = graph.edges(default) if default is not None else []

        widget.set0 = QtCharts.QBarSet(str(default))
        widget.categories = []

        max_value = 0

        for edge in edge_list:
            node_1 = edge[0]
            node_2 = edge[1]
            value = graph[node_1][node_2][prop]
            max_value = value if value > max_value else max_value
            widget.set0.append(value)
            widget.categories.append(str(node_2))

        widget.barSeries = QtCharts.QBarSeries(widget)
        widget.barSeries.append(widget.set0)

        widget.chart = QtCharts.QChart()
        widget.chart.addSeries(widget.barSeries)

        widget.axisX = QtCharts.QBarCategoryAxis()
        widget.axisX.append(widget.categories)

        widget.chart.setAxisX(widget.axisX, widget.barSeries)
        # widget.axisX.setRange("Jan", "Jun")

        widget.axisY = QtCharts.QValueAxis()
        widget.chart.setAxisY(widget.axisY, widget.barSeries)
        widget.axisY.setRange(0, max_value + 2)
        # widget.axisY.setLabelFormat("%.0f")

        if self.run_property.array_name is not None:
            arr = self.result_graph.args[self.run_property.array_name]
            self.chart.setTitle(arrayToString(arr))

        widget.chart.legend().setVisible(True)
        widget.chart.legend().setAlignment(Qt.AlignBottom)

        widget.chartView = QtCharts.QChartView(widget.chart)
        widget.chartView.setRenderHint(QPainter.Antialiasing)

    def draw(self, result_graph):
        self.result_graph = result_graph

        has_attribute = hasattr(self, "chartView")
        if has_attribute:
            # self.chartView.hide()
            self.layout().removeWidget(self.chartView)

            try:
                self.layout().takeAt(2)
            except Exception as error:
                print("not work")
            self.chartView.deleteLater()
            del self.chartView
        else:
            self.combo_box = QComboBox(self)
            self.vertical_layout.addWidget(self.combo_box)
            self.combo_box.addItems([str(node) for node in self.result_graph.graph.nodes()])
            self.combo_box.currentTextChanged.connect(self.update_viewChart)
        self.draw_(self)
        self.layout().addWidget(self.chartView)

        QCoreApplication.processEvents()

    def full_size_mode(self):
        main_widget = QMainWindow(self)
        self.draw_(main_widget)
        main_widget.setCentralWidget(main_widget.chartView)
        main_widget.showMaximized()


    def update_viewChart(self, text):
        self.draw(self.result_graph)


