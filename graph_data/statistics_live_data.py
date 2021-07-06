from PySide2.QtCore import SIGNAL, Signal, QObject, Slot
import typing



class Signals(QObject):

    change_data = Signal()


class Statistics_live_data(QObject):

    def __init__(self):

        super(Statistics_live_data, self).__init__()

        self.signals = Signals()

        self.data = None
        self._data = None
        self.property_name = None
        # self.chart_name = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if value is not None:
            self._data = value
            self.signals.change_data.emit()


if __name__ == '__main__':

    s = Statistics_live_data()
    s.data = "korte"
