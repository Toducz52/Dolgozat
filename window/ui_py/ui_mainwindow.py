# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from window.code_editor.my_code_editor import MyQPlainTextEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(691, 597)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)

        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")

        self.gridLayout.addWidget(self.btn_save, 1, 0, 1, 1)

        self.btn_new_page = QPushButton(self.centralwidget)
        self.btn_new_page.setObjectName(u"btn_new_page")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_new_page.sizePolicy().hasHeightForWidth())
        self.btn_new_page.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_new_page, 1, 3, 1, 1)

        self.btn_save_as = QPushButton(self.centralwidget)
        self.btn_save_as.setObjectName(u"btn_save_as")
        sizePolicy.setHeightForWidth(self.btn_save_as.sizePolicy().hasHeightForWidth())
        self.btn_save_as.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_save_as, 0, 0, 1, 1)

        self.btn_add_edge_function_call_to_code = QPushButton(self.centralwidget)
        self.btn_add_edge_function_call_to_code.setObjectName(u"btn_add_edge_function_call_to_code")

        self.gridLayout.addWidget(self.btn_add_edge_function_call_to_code, 1, 2, 1, 1)

        self.btn_create_function_head = QPushButton(self.centralwidget)
        self.btn_create_function_head.setObjectName(u"btn_create_function_head")

        self.gridLayout.addWidget(self.btn_create_function_head, 0, 2, 1, 1)

        self.btn_static = QPushButton(self.centralwidget)
        self.btn_static.setObjectName(u"btn_static")
        sizePolicy.setHeightForWidth(self.btn_static.sizePolicy().hasHeightForWidth())
        self.btn_static.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_static, 0, 1, 1, 1)

        self.btn_run = QPushButton(self.centralwidget)
        self.btn_run.setObjectName(u"btn_run")
        sizePolicy.setHeightForWidth(self.btn_run.sizePolicy().hasHeightForWidth())
        self.btn_run.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_run, 1, 1, 1, 1)

        # **
        self.btn_save_result = QPushButton(self.centralwidget)
        self.btn_save_result.setObjectName(u"btn_save_result")
        sizePolicy.setHeightForWidth(self.btn_save_result.sizePolicy().hasHeightForWidth())
        self.btn_save_result.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_save_result, 0, 4, 1, 1)
        # **

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.btn_algorithm_handle = QPushButton(self.centralwidget)
        self.btn_algorithm_handle.setObjectName(u"btn_algorithm_handle")

        self.gridLayout.addWidget(self.btn_algorithm_handle, 0, 3, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 0, 5, 1, 1)

        self.btn_stop = QPushButton(self.centralwidget)
        self.btn_stop.setObjectName(u"btn_stop")

        self.gridLayout.addWidget(self.btn_stop, 1, 5, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.out_session_name = QLabel(self.centralwidget)
        self.out_session_name.setObjectName(u"out_session_name")

        self.horizontalLayout_2.addWidget(self.out_session_name)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.in_code = MyQPlainTextEdit(self.centralwidget)
        self.in_code.setObjectName(u"in_code")

        self.verticalLayout.addWidget(self.in_code)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 691, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u" ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Algoritmus vizsg\u00e1l\u00f3", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Ment\u00e9s", None))
        self.btn_new_page.setText(QCoreApplication.translate("MainWindow", "Új munkamenet", None))
        self.btn_save_as.setText(QCoreApplication.translate("MainWindow", u"Ment\u00e9s m\u00e1sk\u00e9nt", None))
        self.btn_add_edge_function_call_to_code.setText(QCoreApplication.translate("MainWindow", u"\u00c9l hozz\u00e1ad\u00e1sa", None))
        self.btn_create_function_head.setText(QCoreApplication.translate("MainWindow", u"Fejl\u00e9c l\u00e9trehoz\u00e1sa ", None))
        self.btn_static.setText(QCoreApplication.translate("MainWindow", u"Statisztika", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Futtat", None))
        self.btn_save_result.setText(QCoreApplication.translate("MainWindow", "Jelenlegi eredmény mentése", None))
        self.btn_algorithm_handle.setText(QCoreApplication.translate("MainWindow", u"Algoritmusok kezel\u00e9se", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"Meg\u00e1ll\u00edt", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Munkamenet neve(ment\u00e9s neve):", None))
        self.out_session_name.setText(QCoreApplication.translate("MainWindow", u"Jelenleg nincs megadva!", None))
        self.in_code.setPlainText(QCoreApplication.translate("MainWindow", u"Megk\u00e9rem el\u0151sz\u0151r adja hozz\u00e1 a fejl\u00e9cet. \n"
"", None))
    # retranslateUi

