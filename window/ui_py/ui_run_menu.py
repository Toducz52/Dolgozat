# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'run_menu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_form(object):
    def setupUi(self, form):
        if not form.objectName():
            form.setObjectName(u"form")
        form.resize(345, 278)
        self.verticalLayout = QVBoxLayout(form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.btn_run_simple = QPushButton(form)
        self.btn_run_simple.setObjectName(u"btn_run_simple")

        self.verticalLayout.addWidget(self.btn_run_simple)

        self.btn_run_all_permutation = QPushButton(form)
        self.btn_run_all_permutation.setObjectName(u"btn_run_all_permutation")

        self.verticalLayout.addWidget(self.btn_run_all_permutation)

        self.btn_run_all_permutation_sum = QPushButton(form)
        self.btn_run_all_permutation_sum.setObjectName(u"btn_run_all_permutation_sum")

        self.verticalLayout.addWidget(self.btn_run_all_permutation_sum)

        self.btn_run_random_array = QPushButton(form)
        self.btn_run_random_array.setObjectName(u"btn_run_random_array")

        self.verticalLayout.addWidget(self.btn_run_random_array)

        self.btn_dance_problem = QPushButton(form)
        self.btn_dance_problem.setObjectName(u"btn_dance_problem")

        self.verticalLayout.addWidget(self.btn_dance_problem)


        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, form):
        form.setWindowTitle(QCoreApplication.translate("form", u"Futtat\u00e1si men\u00fc", None))
        self.label.setText(QCoreApplication.translate("form", u"Futtat\u00e1si m\u00f3dok:", None))
        self.btn_run_simple.setText(QCoreApplication.translate("form", u"Egyszer\u0171 futtat\u00e1s", None))
        self.btn_run_all_permutation.setText(QCoreApplication.translate("form", u"\u00d6sszes permut\u00e1ci\u00f3ra ", None))
        self.btn_run_all_permutation_sum.setText(QCoreApplication.translate("form", u"\u00d6sszes permut\u00e1ci\u00f3ra \u00f6sszes\u00edtve", None))
        self.btn_run_random_array.setText(QCoreApplication.translate("form", u"Egy random t\u00f6mbre ", None))
        self.btn_dance_problem.setText(QCoreApplication.translate("form", u"Saj\u00e1tos, t\u00e1ncos probl\u00e9ma", None))
    # retranslateUi

