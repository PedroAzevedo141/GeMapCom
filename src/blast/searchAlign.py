import os
from Bio import SeqIO, Entrez

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Telas.tela_dialog_search import Ui_DialogSearch


class EmployeeSearch(QDialog):
    """Employee dialog."""

    def __init__(self, ui_main, blast_main, name, type, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_DialogSearch()
        self.ui_main = ui_main
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        
        font = QFont("Consolas", 9)
        self.ui.textEdit_seq.setFont(font)
        
        self.name = name
        self.type = type
        self.handleText = False
        self.blast_main = blast_main
        self.ui.pushButton_search.clicked.connect(self.fetch_seq)
        
    def check_db_selected(self):
        if (self.ui.radioButton_pubmed.isChecked()):
            return "pubmed"
        elif (self.ui.radioButton_protein.isChecked()):
            return "protein"
        elif (self.ui.radioButton_nucleotide.isChecked()):
            return "nucleotide"
        elif (self.ui.radioButton_cancerchromosomes.isChecked()):
            return "cancerchromosomes"
        elif (self.ui.radioButton_ncbisearch.isChecked()):
            return "ncbisearch"
        elif (self.ui.radioButton_nlmcatalog.isChecked()):
            return "nlmcatalog"
        elif (self.ui.radioButton_outro.isChecked()):
            return self.ui.lineEdit_db_outro.text()
        else:
            return None
        
    def fetch_seq(self):
        Entrez.email = self.ui.lineEdit_email.text()
        
        if len(self.ui.lineEdit_ID.text()) > 0:
            try:
            
                self.db = self.check_db_selected()
                self.seq_id = self.ui.lineEdit_ID.text()
                self.rettype = "fasta"
                self.retmode = "text"
                self.filename = self.name + ".fasta"
                
                self.handle = Entrez.efetch(db=self.db, id=self.seq_id,
                                    rettype=self.rettype, retmode=self.retmode)
                
                out_handle = open(self.filename, "w")
                out_handle.write(self.handle.read())
                out_handle.close()
                self.handle.close()
                
                self.record = SeqIO.read(self.filename, "fasta")
                
                self.ui.textEdit_seq.setText(str(self.record))
                
                self.handleText = True
                
            except:
                self.ui.textEdit_seq.clear()
                QMessageBox.about(
                    self, "Alinhamento", "\nAlinhamento nao encontrado!\t\n")
        else:
            QMessageBox.about(
                self, "Aviso", "\nInforme o ID da sequencia!\t\n")
        
        # Entrez.efetch(db="nucleotide", id="EU490707",6273291
        #               rettype="gb", retmode="text")
    
    def accept(self) -> None:

        if self.type == "query" and self.handleText:
            self.blast_main.Query = self.filename
            self.ui_main.NomeArquivoQUERY.setText(self.record.name)
            self.ui_main.CabecalhoArquivoQUERY.setText(self.record.description)
            
        if self.type == "subject" and self.handleText:
            self.blast_main.Subject = self.filename
            self.ui_main.NomeArquivoSUBJECT.setText(self.record.name)
            self.ui_main.CabecalhoArquivoSUBJECT.setText(self.record.description)

        self.ui.textEdit_seq.clear()
        return super().accept()
