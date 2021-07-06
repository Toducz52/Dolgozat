# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_edge_window.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700,500)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setPointSize(20)
        self.label_15.setFont(font)

        self.verticalLayout_2.addWidget(self.label_15)

        self.btn_add_new_row = QPushButton(Form)
        self.btn_add_new_row.setObjectName(u"btn_add_new_row")

        self.verticalLayout_2.addWidget(self.btn_add_new_row)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.btn_delete_row = QPushButton(Form)
        self.btn_delete_row.setObjectName(u"btn_delete_row")

        self.verticalLayout_2.addWidget(self.btn_delete_row)

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u" ", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u00c9l hozz\u00e1ad\u00e1sa: ", None))
        self.btn_add_new_row.setText(QCoreApplication.translate("Form", u"\u00daj sor besz\u00far\u00e1sa a t\u00e1bl\u00e1zatba", None))
        self.btn_delete_row.setText(QCoreApplication.translate("Form", u"Kiv\u00e1lasztott sor t\u00f6rl\u00e9se a t\u00e1bl\u00e1zatb\u00f3l", None))
        self.label.setText(QCoreApplication.translate("Form", u"A kurzort helyezd oda a k\u00f3dszerkeszt\u0151ben, ahova beszeretn\u00e9d illeszteni az \u00e9ll hozz\u00e1ad\u00e1s\u00e1t.", None))
    # retranslateUi

