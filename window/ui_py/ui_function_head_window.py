# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'function_head_window.ui'
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
        Form.resize(563, 393)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.in_function_name = QLineEdit(Form)
        self.in_function_name.setObjectName(u"in_function_name")

        self.verticalLayout.addWidget(self.in_function_name)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.in_parameter = QLineEdit(Form)
        self.in_parameter.setObjectName(u"in_parameter")

        self.verticalLayout.addWidget(self.in_parameter)

        self.btn_add_parameter = QPushButton(Form)
        self.btn_add_parameter.setObjectName(u"btn_add_parameter")

        self.verticalLayout.addWidget(self.btn_add_parameter)

        self.btn_delete_parameter = QPushButton(Form)
        self.btn_delete_parameter.setObjectName(u"btn_delete_parameter")

        self.verticalLayout.addWidget(self.btn_delete_parameter)

        self.list_parameter = QListWidget(Form)
        self.list_parameter.setObjectName(u"list_parameter")

        self.verticalLayout.addWidget(self.list_parameter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.btn_create_function_head = QPushButton(Form)
        self.btn_create_function_head.setObjectName(u"btn_create_function_head")

        self.horizontalLayout_2.addWidget(self.btn_create_function_head)

        self.btn_back = QPushButton(Form)
        self.btn_back.setObjectName(u"btn_back")

        self.horizontalLayout_2.addWidget(self.btn_back)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u" ", None))
        self.label.setText(QCoreApplication.translate("Form", u"F\u00fcggv\u00e9nyfejl\u00e9c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"F\u00fcggv\u00e9nyn\u00e9v:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Param\u00e9terlista:", None))
        self.btn_add_parameter.setText(QCoreApplication.translate("Form", u"Hozz\u00e1ad", None))
        self.btn_delete_parameter.setText(QCoreApplication.translate("Form", u"T\u00f6r\u00f6l", None))
        self.btn_create_function_head.setText(QCoreApplication.translate("Form", u"Fejl\u00e9c l\u00e9trehoz\u00e1sa vagy modositasa", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"Vissza", None))
    # retranslateUi

