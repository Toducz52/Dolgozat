from graph_data.statistics_live_data import Statistics_live_data
import sys
from graph_data.result_run_simple import Result_run_simple
import traceback
from window.statistics_menu_window import Statistics_menu_window
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QGridLayout
from PySide2.QtCore import Slot, SIGNAL, QObject, Signal, Qt
from window.ui_py.ui_mainwindow import Ui_MainWindow
from util.util_regex import *
# from builder_method.build_algorithm import FactoryWrappedAlgorithm
from util.util_msg_box import create_simple_message_box_and_run
from util.util_mainwindow import get_parameter_list_and_f_name_in_f_header
from window.function_head_window import Function_head_window
from window.create_edge_window import Create_edge_window
from db.DB import *
from window.save_window import Save_window
from window.load_window import Load_window
from window.run_menu_window import Run_menu_window
from graph_data.result_run import Result_run
from util.util_graph_helper import attrsToString
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

from window.statistics_view import Statistics_view

from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


class MainWindow(QMainWindow):
    signal_pushButtonAdd = Signal(str, str, str)
    signal_pushButtonDelete = Signal(str, str, str)

    def __init__(self):
        super(MainWindow, self).__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.parameter_list = []
        self.function_head_window = Function_head_window(self)
        self.create_edge_window = Create_edge_window(self)
        self.load_window = None
        self.save_window = None
        self.session_name = None
        self.run_menu = None
        self.result_run = Result_run.getInstance()
        self.statistics_view = None
        self.load_alg_wrapper = None
        self.statistics_menu = None
        self.result_run2 = None

        QObject.connect(self.ui.btn_add_edge_function_call_to_code, SIGNAL('clicked()'), self.show_create_edge_window)
        QObject.connect(self.ui.btn_create_function_head, SIGNAL('clicked()'), self.show_function_head_window)
        self.ui.btn_algorithm_handle.clicked.connect(self.show_load_window)
        self.ui.btn_save_as.clicked.connect(self.save_as)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_run.clicked.connect(self.show_run_menu_window)
        self.ui.btn_new_page.clicked.connect(self.new_page)
        self.ui.btn_save_result.clicked.connect(self.save_temporary_result)


        self.signal = self.result_run.get_signal()
        self.signal.connect(self.result_handle)

        self.signal = self.result_run.get_signal_show_progress_bar()
        self.signal.connect(self.show_progress_bar)

        self.signal = self.result_run.get_signal_hide_progress_bar()
        self.signal.connect(self.hide_progress_bar)

        self.signal = self.result_run.get_signal_change_progress_bar()
        self.signal.connect(self.change_progress_bar)

        self.signal = self.result_run.get_signal_infinite_progress_bar()
        self.signal.connect(self.set_infinite_progress_bar)

        self.signal = self.result_run.get_signal_error()
        self.signal.connect(self.run_error_handle)

        self.ui.btn_stop.clicked.connect(self.stop_run)

        self.repo = self.initialization_database()

        self.ui.progressBar.hide()
        self.ui.btn_stop.hide()

        self.ui.btn_static.clicked.connect(self.show_statistics_menu)

        self.statistics_live_data = Statistics_live_data()
        self.statistics_live_data.signals.change_data.connect(self.show_statistics)

    @Slot()
    def save_temporary_result(self):

        if self.result_run2 is not None:
            print(self.result_run2.result[0].graph.edges())

        if len(self.result_run.result) == 0:
            create_simple_message_box_and_run(self, "Nincs lefuttatott eredmény.")
            return None
        else:
            self.result_run2 = Result_run_simple(self.result_run)

            self.ui.btn_save_result.setStyleSheet("QPushButton"
                                 "{"
                                 "background-color : lightblue;"
                                 "}"
                                 "QPushButton::pressed"
                                 "{"
                                 "background-color : red;"
                                 "}"
                                 )

    def print_two_result(self):
        pass

    @Slot()
    def run_error_handle(self, error):
        print(error)
        create_simple_message_box_and_run(self, error)

    @Slot()
    def show_statistics(self):

        self.statistics_view = Statistics_view(self)
        self.statistics_view.showMaximized()

    @Slot()
    def show_statistics_menu(self):
        if self.statistics_menu is None:
            self.statistics_menu = Statistics_menu_window(self)
        self.statistics_menu.show()

    def set_infinite_progress_bar(self, flag):

        # print(flag)

        self.ui.progressBar.setMinimum(0)

        if flag:
            self.ui.progressBar.setMaximum(0)
        else:
            self.ui.progressBar.setMaximum(100)

    @Slot()
    def result_handle(self):
        # print("Koszonom Istenem vege!")
        pass

    @Slot()
    def show_progress_bar(self):

        self.ui.btn_stop.show()
        self.ui.progressBar.show()
        self.ui.progressBar.setValue(0)

    @Slot()
    def hide_progress_bar(self):

        self.ui.btn_stop.hide()
        self.ui.progressBar.hide()

    @Slot()
    def change_progress_bar(self, value):

        self.ui.progressBar.setValue(value)

    def stop_run(self):
        try:
            self.run_menu.add_parameters_window.worker_thread.stop()
        except:
            traceback.print_exc()

    def initialization_database(self):
        dao = DAO(DB)
        repo = Repository(dao)
        return repo

    def get_algorithm_data(self):
        pass

    @Slot()
    def save_as(self):
        self.save_window = Save_window(self)
        self.save_window.show()

    @Slot()
    def save(self):

        if self.session_name is None:
            self.save_as()
        else:
            if self.save_window is None:
                self.save_window = Save_window(self)
            self.save_window.save()

    @Slot()
    def show_run_menu_window(self):
        if self.run_menu is None:
            self.run_menu = Run_menu_window(self)
            self.run_menu.show()
        else:
            if not self.ui.progressBar.isVisible():
                self.run_menu.show()

    @Slot()
    def show_create_edge_window(self):
        self.create_edge_window.show()

    @Slot()
    def show_function_head_window(self):
        self.function_head_window.show()

    @Slot()
    def show_load_window(self):
        self.load_window = Load_window(self)
        self.load_window.show()

    @Slot()
    def btn_run(self):

        code = self.ui.in_code.toPlainText()
        function_name = self.ui.in_function_name.text()

        error = ''

        if code == "":
            error = error + "Adjon meg egy kódot.\n"

        function_header = first_match(code, ".*\n")
        if function_header:
            if not is_valid_function_head(function_header):
                error = error + "Helytelen függvény fejléc."
            else:
                function_name, self.parameter_list = get_parameter_list_and_f_name_in_f_header(function_header)
                # print(self.parameter_list)

        if not is_valid_function_name(function_name):
            error = error + "Helytelen függvény nev.\n"

        if len(self.parameter_list) == 0:
            error = "A paraméterlista legalább egy tömböt kell tartalmazzon.\n"

        if error == '':
            try:
                # build_sort = FactoryWrappedAlgorithm(code, function_name, self.parameter_list)
                # build_sort.args['arr'] = [3, 2, 1]
                # build_sort.args['n'] = 3
                # build_sort.callbackSort(build_sort.args)
                # print(build_sort.args['arr'])
                pass
            except Exception as er:
                create_simple_message_box_and_run(self, str(er))
        else:
            create_simple_message_box_and_run(self, error)

    def create_algorithm_wrapper(self) -> Algorithm_wrapper:

        """def initialization(self, save_name, function_name, readme, code, function_call, args=None,
                       update_date=None, create_date=None):"""

        save = Save_window(self)
        save_name, function_head_detail, code, function_calls, readme = save.get_data()
        return Algorithm_wrapper().initialization(save_name, function_head_detail.function_name, readme, code,
                                                  function_calls, function_head_detail.args)
    @Slot()
    def new_page(self):
        self.parameter_list = []
        self.function_head_window = Function_head_window(self)
        self.create_edge_window = Create_edge_window(self)
        self.load_window = None
        self.save_window = None
        self.session_name = None
        self.run_menu = None

        self.statistics_menu = None

        self.statistics_view = None

        self.load_alg_wrapper = None

        self.ui.in_code.signal_not_work = True
        self.ui.in_code.setPlainText("Megkérem előszőr adja hozzá a fejlécet.")
        self.ui.in_code.clearValue()
        self.ui.in_code.signal_not_work = False
        self.ui.in_code.setReadOnly(True)

        del self.result_run

        self.result_run = Result_run.getInstance()

        self.ui.out_session_name.setText("Jelenleg nincs megadva.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    # https://www.geeksforgeeks.org/defining-a-python-function-at-runtime/

    sys.exit(app.exec_())
