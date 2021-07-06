from PySide2.QtWidgets import QPushButton, QWidget, QVBoxLayout, QApplication, QLabel, QSizePolicy
from functools import partial
from PySide2.QtCore import Qt
from window.add_parameters_window import Add_parameters_window
from util.util_msg_box import create_simple_message_box_and_run

class Run_menu_window(QWidget):

    mapping = {'Egyszerű futtatás': 'run_simple',
               'Algoritmus lefuttatása egy tömb összes permutációjára ': 'run_all_permutation',
               'Algoritmus lefuttatása egy tömb összes permutációjára, majd ennek az összege': 'run_all_permutation_sum',
               'Egy random tömbre az algoritmus lefuttatása': 'run_random_array',
               'Algoritmus futtatása, majd ebből felépülő gráf szinezése': 'run_drawing_with_colors'
               }

    def __init__(self, parent):
        QWidget.__init__(self)
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        self.parent = parent
        self.add_parameters_window = None
        self.label = QLabel(self)
        self.label.setText("Elemzési módszer kiválasztása:")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label.setStyleSheet("font: 15pt")
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        layout.addWidget(self.label)
        self.buttons = []
        for key, value in Run_menu_window.mapping.items():
            self.buttons.append(QPushButton(key, self))
            self.buttons[-1].clicked.connect(partial(self.handleButton, func=value))
            layout.addWidget(self.buttons[-1])

    def handleButton(self, func="\n"):
        # print(func)
        if self.add_parameters_window is not None:
            self.hide()
            del self.add_parameters_window

        try:

            self.add_parameters_window = Add_parameters_window(self, func)
            self.add_parameters_window.show()
        except Exception as error:
            create_simple_message_box_and_run(self, str(error))

