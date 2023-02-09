from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Telas.qDialogBlast import Ui_Dialog_Custom

class EmployeeDlg(QDialog):
    """Employee dialog."""

    def __init__(self, ui_main, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog_Custom()
        self.ui_main = ui_main
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)

    def accept(self) -> None:

        if self.ui.radioButton_blastn.isChecked():
            self.ui_main.type_blast = "blastn"
        elif self.ui.radioButton_blastp.isChecked():
            self.ui_main.type_blast = "blastp"
        elif self.ui.radioButton_blastx.isChecked():
            self.ui_main.type_blast = "blastx"
        elif self.ui.radioButton_tblastx.isChecked():
            self.ui_main.type_blast = "tblastx"
        elif self.ui.radioButton_tblastn.isChecked():
            self.ui_main.type_blast = "tblastn"
        elif self.ui.radioButton_psiblast.isChecked():
            self.ui_main.type_blast = "psiblast"

        return super().accept()
