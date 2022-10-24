import os
import sys
from PySide6.QtWidgets import *      # type: ignore
from PySide6.QtCore import QCoreApplication
from screens.ui_mainwindow import Ui_MainWindow
import pyperclip as clip
from traduction.traduction import traduzir, lerArquivo
from traduction.dict import lerListadeLinguagens


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        #######################################
        #Configurações da GUI
        #######################################
        self.setupUi(self)
        self.setWindowTitle("TransPy - Tradutor de PDF")
        self.dict = lerListadeLinguagens()
        try: 
            self.keysDict = list(self.dict.keys())   # type: ignore
        except:
             
            while True:
                print("Não foi possível ler o arquivo 'languagestotraduction.json', tentando novamente...")
                try :self.keysDict = list(self.dict.keys())   # type: ignore
                except: pass
                
                if self.keysDict != None:
                    break       
        
        
        self.cbLingua.addItems(self.keysDict)
        
        
        #######################################
        #Ações dos botões
        #######################################
        self.btnProcurarArquivo.clicked.connect(self.procurarArquivo)  # type: ignore
        self.btnCopiarTextoPDF.clicked.connect(self.copiarTextoPDF)  # type: ignore
        self.btnCopiarTextoTraduzido.clicked.connect(self.copiarTextoTraduzido)  # type: ignore
        self.btnTraduzir.clicked.connect(self.traduzirTXT)            # type: ignore
                
    def procurarArquivo(self):
        self.arquivo = QFileDialog.getOpenFileName(self, "Open PDF", os.getcwd(), "PDF Files (*.pdf)" )[0]
        
        self.lblNomeDoArquivo.setText(QCoreApplication.translate("MainWindow", self.arquivo, None))
       
        lerArquivo(arquivo=self.arquivo)
        
        pdfFile = open(os.getcwd() + '/files/pdfFile.txt', "r", encoding="utf-8")
        texto = pdfFile.read()
        pdfFile.close
        
        self.enTextoPDF.setText(QCoreApplication.translate("MainWindow", texto, None))
    
    def traduzirTXT(self):
        linguaSelecionada = self.cbLingua.currentText()
        
        if linguaSelecionada == "Default (English)":
            linguaSelecionada = "English (english)"
        
        textoLido = self.enTextoPDF.text()
        
        print(textoLido)
        
        traducao = traduzir(texto=textoLido , linguaSelecionada= self.dict[linguaSelecionada])   # type: ignore
        
        self.enTextoTraduzido.setText(QCoreApplication.translate("MainWindow", traducao, None))
        
    def copiarTextoPDF(self):
        textoPDF = self.enTextoPDF.text()
        
        clip.copy(textoPDF)
        
        print("\033[0;49;92mCopiado com sucesso! \033[m")
    
    def copiarTextoTraduzido(self):
        textoTraduzido = self.enTextoTraduzido.text()
        
        clip.copy(textoTraduzido)
        
        
        print("\033[0;49;92mCopiado com sucesso! \033[m")
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
