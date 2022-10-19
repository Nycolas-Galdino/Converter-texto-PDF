from logging import warning
import os
import sys
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import *
from screens.ui_mainwindow import Ui_MainWindow
import pyperclip as clip
from traduction.traduction import traduzir


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        #######################################
        #Configurações da GUI
        #######################################
        self.setupUi(self)
        self.setWindowTitle("TransPy - Tradutor de PDF")
        
        #######################################
        #Ações dos botões
        #######################################
        self.btnProcurarArquivo.clicked.connect(self.procurarArquivo)
        self.btnCopiarTextoPDF.clicked.connect(self.copiarTextoPDF)
        self.btnCopiarTextoTraduzido.clicked.connect(self.copiarTextoTraduzido)
        self.btnTraduzir.clicked.connect(self.traduzirPDF)          
                
    def procurarArquivo(self):
        self.arquivo = QFileDialog.getOpenFileName(self, "Open PDF", os.getcwd(), "PDF Files (*.pdf)" )[0]
        self.lblNomeDoArquivo.setText(self.arquivo)
        
        return self.arquivo
    
    def traduzirPDF(self):
        tradução = traduzir(arquivo= self.arquivo, linguaSelecionada= self.cbLingua.currentText())
        
        pdfFile = open(os.getcwd() + '/files/pdfFile.txt', "r", encoding="utf-8")
        texto = pdfFile.read()
        pdfFile.close
        
        self.lblTextoPDF.setText(texto)
        
        
        self.lblTextoTraduzido.setText(tradução)
        
    def copiarTextoPDF(self):
        textoPDF = self.lblTextoPDF.text()
        
        clip.copy(textoPDF)
        
        print("\033[0;49;92mCopiado com sucesso! \033[m")
    
    def copiarTextoTraduzido(self):
        textoTraduzido = self.lblTextoTraduzido.text()
        
        clip.copy(textoTraduzido)
        
        
        print("\033[0;49;92mCopiado com sucesso! \033[m")
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())