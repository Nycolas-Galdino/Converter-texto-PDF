from logging import warning
import os
import sys
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import *
from screens.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        self.setupUi(self)
        self.setWindowTitle("TransPy - Tradutor de PDF")
        
        self.btnProcurarArquivo.clicked.connect(self.procurarArquivo)
        
    def procurarArquivo(self):
        self.arquivo = QFileDialog.getOpenFileName(self, "Open PDF", os.getcwd(), "PDF Files (*.pdf)" )[0]
        return self.arquivo
    
    def traduzirPDF(self):
        pass
    
    def copiarTextoPDF(self):
        pass
    
    def copiarTextoTraduzido(self):
        pass
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())