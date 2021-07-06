# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_window.ui'
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
        Form.resize(496, 457)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.out_readme = QTextBrowser(Form)
        self.out_readme.setObjectName(u"out_readme")

        self.verticalLayout.addWidget(self.out_readme)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.out_function_name = QLabel(Form)
        self.out_function_name.setObjectName(u"out_function_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.out_function_name)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.out_create_date = QLabel(Form)
        self.out_create_date.setObjectName(u"out_create_date")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.out_create_date)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.out_update_date = QLabel(Form)
        self.out_update_date.setObjectName(u"out_update_date")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.out_update_date)

        self.out_save_name = QLabel(Form)
        self.out_save_name.setObjectName(u"out_save_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.out_save_name)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_delete = QPushButton(Form)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout_3.addWidget(self.btn_delete)

        self.btn_load = QPushButton(Form)
        self.btn_load.setObjectName(u"btn_load")

        self.horizontalLayout_3.addWidget(self.btn_load)

        self.btn_back = QPushButton(Form)
        self.btn_back.setObjectName(u"btn_back")

        self.horizontalLayout_3.addWidget(self.btn_back)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u" ", None))
        self.label.setText(QCoreApplication.translate("Form", u"Algoritmus bet\u00f6lt\u00e9se vagy v\u00e9gleges t\u00f6rl\u00e9se", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Algoritmusok:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Megjegyz\u00e9s:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Ment\u00e9s:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"F\u00fcggv\u00e9ny n\u00e9v:", None))
        self.out_function_name.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"L\u00e9trehoz\u00e1s d\u00e1tuma:", None))
        self.out_create_date.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Friss\u00edt\u00e9s d\u00e1tuma", None))
        self.out_update_date.setText("")
        self.out_save_name.setText("")
        self.btn_delete.setText(QCoreApplication.translate("Form", u"V\u00e9gleg t\u00f6r\u00f6l", None))
        self.btn_load.setText(QCoreApplication.translate("Form", u"Bet\u00f6lt", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"Vissza", None))
    # retranslateUi

