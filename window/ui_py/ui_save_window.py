# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_window.ui'
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
        Form.resize(425, 299)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.in_save_name = QLineEdit(Form)
        self.in_save_name.setObjectName(u"in_save_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.in_save_name)


        self.verticalLayout.addLayout(self.formLayout)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.in_readme = QPlainTextEdit(Form)
        self.in_readme.setObjectName(u"in_readme")

        self.verticalLayout.addWidget(self.in_readme)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.btn_save = QPushButton(Form)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.btn_back = QPushButton(Form)
        self.btn_back.setObjectName(u"btn_back")

        self.horizontalLayout_2.addWidget(self.btn_back)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u" ", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ment\u00e9s", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Ment\u00e9s neve:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Megjegyz\u00e9s", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"Ment\u00e9s", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"Vissza", None))
    # retranslateUi

