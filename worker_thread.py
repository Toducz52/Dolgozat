# Create the Worker Thread
import traceback
import time
import sys
from PySide2.QtCore import QObject, QThread, Signal, Slot
from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from runner.runner_algorithm import start
from util.util_msg_box import create_detail_message_box

class WorkerThread(QThread):
    def __init__(self, parent=None, controller_function=None, run_property=None, result=None):
        QThread.__init__(self, parent)
        # Instantiate signals and connect signals to the slots

        self.controller_function = controller_function
        self.result = result
        self.result.run_property = run_property
        self.parent = parent
        self.error = None

    def run(self):

        self.result.emit_signal_show_progress_bar()
        self.result.emit_signal_infinite_progress_bar(True)

        if self.controller_function != 'run_drawing_with_colors':
            self.result.clear_result()

        try:
            start(self.controller_function, self.result.run_property, self.result)
        except Exception as err:
            self.result.emit_signal_error(str(err))

        self.result.emit_signal()

        self.result.emit_signal_hide_progress_bar()

    def stop(self):
        self.terminate()
        self.result.emit_signal_hide_progress_bar()

