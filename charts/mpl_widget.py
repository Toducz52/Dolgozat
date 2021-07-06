from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QGridLayout
from PySide2.QtCore import Qt
from charts.chart_interface import Chart_abstract


from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random


def arrayToString(arr):
    s = ''
    for i in arr:
        s += str(i) + ' '
    return s

class MplWidget(Chart_abstract):

    def draw_(self, result_graph, fig, run_property):
        graph = result_graph.graph
        args = result_graph.args

        axs = fig.gca()

        pos = nx.spring_layout(graph)

        nx.draw(graph, pos, ax=axs, edge_color='black', width=1, linewidths=1,
                node_size=100, node_color='pink', alpha=0.9,
                labels={node: node for node in graph.nodes()})

        labels = nx.get_edge_attributes(graph, self.prop)
        nx.draw_networkx_edge_labels(graph, pos, ax=axs, edge_labels=labels, font_color='red')

        # axs.set_title("Koszonom Julit")

        # if run_property.array_name is not None:
        #     arr = args[run_property.array_name]
        #     fig.suptitle(arrayToString(arr), fontsize=16)

    def draw(self, result_graph):

        self.result_graph = result_graph

        if self.fig is None:
            self.fig = plt.figure()
            self.canvas = FigureCanvas(self.fig)


            self.vertical_layout.addWidget(self.canvas)

        else:
            self.fig.clear()

        if self.run_property.array_name is not None:
            arr = self.result_graph.args[self.run_property.array_name]
            self.fig.suptitle(arrayToString(arr), fontsize=10)

        self.draw_(result_graph, self.fig, self.run_property)

        self.canvas.draw()

        plt.close()

    def __init__(self, parent, run_property):

        super().__init__(parent, run_property)

        self.fig = None

        plt.close()

    def full_size_mode(self):

        plt.close()

        fig = plt.figure()

        self.draw_(self.result_graph, fig, self.run_property)

        figManager = plt.get_current_fig_manager()
        # figManager.resize(*figManager.window.maxsize())
        figManager.window.showMaximized()

        plt.show()




