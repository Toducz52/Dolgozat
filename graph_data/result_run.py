from PySide2.QtCore import SIGNAL, Signal, QObject
from graph_data.result_graph import Result_graph
from graph_data.run_property import Run_property


class Result_run(QObject):

    __instance = None
    __signal_result = Signal()
    __signal_show_progress_bar = Signal()
    __signal_hide_progress_bar = Signal()
    __signal_change_progress_bar = Signal(int)
    __signal_infinite_progress_bar = Signal(bool)
    __signal_error = Signal(str)

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            Result_run()
        return Result_run.__instance

    def __init__(self):
        if Result_run.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            super().__init__()
            Result_run.__instance = self
            self.result = []
            self.run_property = Run_property()

    def swap_result(self, result):
        self.result = result

    @classmethod
    def get_signal(cls):
        if cls.__instance is None:
            Result_run()
        return cls.__instance.__signal_result

    @classmethod
    def get_signal_show_progress_bar(cls):
        if cls.__instance is None:
            Result_run()
        return cls.__instance.__signal_show_progress_bar

    @classmethod
    def get_signal_hide_progress_bar(cls):
        if cls.__instance is None:
            Result_run()
        return cls.__instance.__signal_hide_progress_bar

    @classmethod
    def get_signal_change_progress_bar(cls):
        if cls.__instance is None:
            Result_run()
        return cls.__instance.__signal_change_progress_bar

    @classmethod
    def emit_signal(cls):
        if cls.__instance is None:
            Result_run()
        cls.__instance.__signal_result.emit()


    @classmethod
    def emit_signal_show_progress_bar(cls):
        if cls.__instance is None:
            Result_run()
        cls.__instance.__signal_show_progress_bar.emit()

    @classmethod
    def emit_signal_hide_progress_bar(cls):
        if cls.__instance is None:
            Result_run()
        cls.__instance.__signal_hide_progress_bar.emit()

    @classmethod
    def emit_signal_change_progress_bar(cls, value):
        if cls.__instance is None:
            Result_run()
        cls.__instance.__signal_change_progress_bar.emit(value)

    @classmethod
    def emit_signal_infinite_progress_bar(cls, flag):
        if cls.__instance is None:
            Result_run()
        cls.__instance.__signal_infinite_progress_bar.emit(flag)

    @classmethod
    def get_signal_infinite_progress_bar(cls):
        if cls.__instance is None:
            Result_run()
        return cls.__instance.__signal_infinite_progress_bar

    @classmethod
    def emit_signal_error(cls, error):
        if cls.__instance is None:
            Result_run()
        cls.__instance.__signal_error.emit(error)

    @classmethod
    def get_signal_error(cls):
        if cls.__instance is None:
            Result_run()
        return cls.__instance.__signal_error

    def __str__(self):
        return str(self.result)

    def add_result_graph(self, result_graph):
        self.result.append(result_graph)

    def clear_result(self):
        self.result.clear()


if __name__ == '__main__':

    s = Result_run.getInstance()
    print(s)

