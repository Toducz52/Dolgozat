from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QGridLayout
from util.util_graph_helper import separate_graph_with_attr
from graph_data.result_graph import Result_graph

class Chart_abstract(QWidget):

    class_name = None

    """draw the chart"""
    def draw(self, result_graph):
        pass

    """call final when want to use draw"""
    def final(self, result_graph):

        self.result_graph = result_graph

        self.vertical_layout = QVBoxLayout()

        self.button = QPushButton(self)
        self.vertical_layout.addWidget(self.button)
        self.button.clicked.connect(self.full_size_mode)
        self.button.setText("Full size mode")
        self.setLayout(self.vertical_layout)

        graph = Result_graph(separate_graph_with_attr(result_graph.graph, self.prop), result_graph.args)

        self.draw(graph)

    def __init__(self, parent, run_property):
        QWidget.__init__(self, parent)

        # fig, ax = plt.subplots()

        self.result_graph = None

        self.run_property = run_property

        self.parent = parent

        self.prop = self.parent.parent.statistics_live_data.property_name

        self.result2 = self.parent.parent.result_run2


    def full_size_mode(self):
        pass


