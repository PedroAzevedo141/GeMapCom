# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'designersfKDtu.ui'
##
# Created by: Qt User Interface Compiler version 5.15.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog_Custom(object):
    def setupUi(self, Dialog_Custom):
        if not Dialog_Custom.objectName():
            Dialog_Custom.setObjectName(u"Dialog_Custom")
        Dialog_Custom.resize(400, 300)
        self.gridLayout = QGridLayout(Dialog_Custom)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog_Custom)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_blastn = QRadioButton(Dialog_Custom)
        self.radioButton_blastn.setObjectName(u"radioButton_blastn")
        self.radioButton_blastn.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_blastn)

        self.radioButton_blastp = QRadioButton(Dialog_Custom)
        self.radioButton_blastp.setObjectName(u"radioButton_blastp")

        self.verticalLayout.addWidget(self.radioButton_blastp)

        self.radioButton_blastx = QRadioButton(Dialog_Custom)
        self.radioButton_blastx.setObjectName(u"radioButton_blastx")

        self.verticalLayout.addWidget(self.radioButton_blastx)

        self.radioButton_tblastx = QRadioButton(Dialog_Custom)
        self.radioButton_tblastx.setObjectName(u"radioButton_tblastx")

        self.verticalLayout.addWidget(self.radioButton_tblastx)

        self.radioButton_tblastn = QRadioButton(Dialog_Custom)
        self.radioButton_tblastn.setObjectName(u"radioButton_tblastn")

        self.verticalLayout.addWidget(self.radioButton_tblastn)

        self.radioButton_psiblast = QRadioButton(Dialog_Custom)
        self.radioButton_psiblast.setObjectName(u"radioButton_psiblast")

        self.verticalLayout.addWidget(self.radioButton_psiblast)

        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog_Custom)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Close | QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog_Custom)
        self.buttonBox.accepted.connect(Dialog_Custom.accept)
        self.buttonBox.rejected.connect(Dialog_Custom.reject)

        QMetaObject.connectSlotsByName(Dialog_Custom)
    # setupUi

    def retranslateUi(self, Dialog_Custom):
        Dialog_Custom.setWindowTitle(
            QCoreApplication.translate("Dialog_Custom", u"Dialog", None))
        self.label.setText(QCoreApplication.translate(
            "Dialog_Custom", u"Qual \u00e9 o tipo de alinhamento?", None))
        self.radioButton_blastn.setText(
            QCoreApplication.translate("Dialog_Custom", u"BLASTN", None))
        self.radioButton_blastp.setText(
            QCoreApplication.translate("Dialog_Custom", u"BLASTP", None))
        self.radioButton_blastx.setText(
            QCoreApplication.translate("Dialog_Custom", u"BLASTX", None))
        self.radioButton_tblastx.setText(
            QCoreApplication.translate("Dialog_Custom", u"TBLASTX", None))
        self.radioButton_tblastn.setText(
            QCoreApplication.translate("Dialog_Custom", u"TBLASTN", None))
        self.radioButton_psiblast.setText(
            QCoreApplication.translate("Dialog_Custom", u"PSIBLAST", None))
    # retranslateUi
