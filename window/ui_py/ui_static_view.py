# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'static_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        Form.resize(528, 421)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.out_set_mode = QLabel(Form)
        self.out_set_mode.setObjectName(u"out_set_mode")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.out_set_mode.sizePolicy().hasHeightForWidth())
        self.out_set_mode.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.out_set_mode)

        self.out_set_graph_name = QLabel(Form)
        self.out_set_graph_name.setObjectName(u"out_set_graph_name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.out_set_mode.sizePolicy().hasHeightForWidth())
        self.out_set_graph_name.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.out_set_graph_name)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.btn_back = QPushButton(Form)
        self.btn_back.setObjectName(u"btn_back")
        sizePolicy2.setHeightForWidth(self.btn_back.sizePolicy().hasHeightForWidth())
        self.btn_back.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_back, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_exit = QPushButton(Form)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy2.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_exit, 0, Qt.AlignBottom)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_next = QPushButton(Form)
        self.btn_next.setObjectName(u"btn_next")
        sizePolicy2.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btn_next, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u" ", None))
        self.label.setText(QCoreApplication.translate("Form", u"Statisztika", None))
        self.out_set_mode.setText(QCoreApplication.translate("Form", u"M\u00f3d: Almafa", None))
        self.btn_back.setText(QCoreApplication.translate("Form", u"Vissza", None))
        self.btn_exit.setText(QCoreApplication.translate("Form", u"Kil\u00e9p", None))
        self.btn_next.setText(QCoreApplication.translate("Form", u"Tov\u00e1bb", None))
    # retranslateUi

