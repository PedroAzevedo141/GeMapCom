# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'tela_dialog_searchSyizTw.ui'
##
# Created by: Qt User Interface Compiler version 5.15.3
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_DialogSearch(object):
    def setupUi(self, DialogSearch):
        if not DialogSearch.objectName():
            DialogSearch.setObjectName(u"DialogSearch")
        DialogSearch.setWindowModality(Qt.WindowModal)
        DialogSearch.resize(673, 480)
        DialogSearch.setModal(True)
        self.gridLayout = QGridLayout(DialogSearch)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_email = QLabel(DialogSearch)
        self.label_email.setObjectName(u"label_email")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_email.sizePolicy().hasHeightForWidth())
        self.label_email.setSizePolicy(sizePolicy)
        self.label_email.setMinimumSize(QSize(131, 17))

        self.verticalLayout.addWidget(self.label_email, 0, Qt.AlignHCenter)

        self.lineEdit_email = QLineEdit(DialogSearch)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit_email)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.line = QFrame(DialogSearch)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_email_2 = QLabel(DialogSearch)
        self.label_email_2.setObjectName(u"label_email_2")
        sizePolicy.setHeightForWidth(
            self.label_email_2.sizePolicy().hasHeightForWidth())
        self.label_email_2.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_email_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_pubmed = QRadioButton(DialogSearch)
        self.radioButton_pubmed.setObjectName(u"radioButton_pubmed")

        self.horizontalLayout.addWidget(self.radioButton_pubmed)

        self.radioButton_protein = QRadioButton(DialogSearch)
        self.radioButton_protein.setObjectName(u"radioButton_protein")

        self.horizontalLayout.addWidget(self.radioButton_protein)

        self.radioButton_nucleotide = QRadioButton(DialogSearch)
        self.radioButton_nucleotide.setObjectName(u"radioButton_nucleotide")

        self.horizontalLayout.addWidget(self.radioButton_nucleotide)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_cancerchromosomes = QRadioButton(DialogSearch)
        self.radioButton_cancerchromosomes.setObjectName(
            u"radioButton_cancerchromosomes")

        self.horizontalLayout_2.addWidget(self.radioButton_cancerchromosomes)

        self.radioButton_ncbisearch = QRadioButton(DialogSearch)
        self.radioButton_ncbisearch.setObjectName(u"radioButton_ncbisearch")

        self.horizontalLayout_2.addWidget(self.radioButton_ncbisearch)

        self.radioButton_nlmcatalog = QRadioButton(DialogSearch)
        self.radioButton_nlmcatalog.setObjectName(u"radioButton_nlmcatalog")

        self.horizontalLayout_2.addWidget(self.radioButton_nlmcatalog)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_outro = QRadioButton(DialogSearch)
        self.radioButton_outro.setObjectName(u"radioButton_outro")

        self.horizontalLayout_4.addWidget(self.radioButton_outro)

        self.lineEdit_db_outro = QLineEdit(DialogSearch)
        self.lineEdit_db_outro.setObjectName(u"lineEdit_db_outro")
        self.lineEdit_db_outro.setEnabled(False)
        self.lineEdit_db_outro.setAcceptDrops(True)
        self.lineEdit_db_outro.setAutoFillBackground(False)
        self.lineEdit_db_outro.setFrame(True)
        self.lineEdit_db_outro.setEchoMode(QLineEdit.Normal)
        self.lineEdit_db_outro.setDragEnabled(False)
        self.lineEdit_db_outro.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_db_outro)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_ID = QLabel(DialogSearch)
        self.label_ID.setObjectName(u"label_ID")

        self.horizontalLayout_3.addWidget(self.label_ID)

        self.lineEdit_ID = QLineEdit(DialogSearch)
        self.lineEdit_ID.setObjectName(u"lineEdit_ID")

        self.horizontalLayout_3.addWidget(self.lineEdit_ID)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_search = QPushButton(DialogSearch)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton_search)

        self.line_2 = QFrame(DialogSearch)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.textEdit_seq = QTextEdit(DialogSearch)
        self.textEdit_seq.setObjectName(u"textEdit_seq")
        self.textEdit_seq.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEdit_seq)

        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.buttonBox = QDialogButtonBox(DialogSearch)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout_5.addWidget(self.buttonBox)

        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(DialogSearch)
        self.buttonBox.accepted.connect(DialogSearch.accept)
        self.buttonBox.rejected.connect(DialogSearch.reject)
        self.radioButton_outro.toggled.connect(
            self.lineEdit_db_outro.setEnabled)

        QMetaObject.connectSlotsByName(DialogSearch)
    # setupUi

    def retranslateUi(self, DialogSearch):
        DialogSearch.setWindowTitle(
            QCoreApplication.translate("DialogSearch", u"Search", None))
        self.label_email.setText(QCoreApplication.translate(
            "DialogSearch", u"Informe seu e-mail:", None))
        self.label_email_2.setText(QCoreApplication.translate(
            "DialogSearch", u"Informe o database:", None))
        self.radioButton_pubmed.setText(
            QCoreApplication.translate("DialogSearch", u"PubMed", None))
        self.radioButton_protein.setText(
            QCoreApplication.translate("DialogSearch", u"Protein", None))
        self.radioButton_nucleotide.setText(
            QCoreApplication.translate("DialogSearch", u"Nucleotide", None))
        self.radioButton_cancerchromosomes.setText(
            QCoreApplication.translate("DialogSearch", u"Cancer Chromosomes", None))
        self.radioButton_ncbisearch.setText(
            QCoreApplication.translate("DialogSearch", u"NCBI Search", None))
        self.radioButton_nlmcatalog.setText(
            QCoreApplication.translate("DialogSearch", u"NLM Catalog", None))
        self.radioButton_outro.setText(
            QCoreApplication.translate("DialogSearch", u"Outro", None))
        self.label_ID.setText(QCoreApplication.translate(
            "DialogSearch", u"ID:", None))
        self.pushButton_search.setText(
            QCoreApplication.translate("DialogSearch", u"Search", None))
    # retranslateUi
