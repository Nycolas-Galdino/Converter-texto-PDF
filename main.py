import os
import sys
from PySide6.QtWidgets import *      # type: ignore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from screens.ui_mainwindow import Ui_MainWindow
import pyperclip as clip
from traduction.traduction import traduzir, lerArquivo
from traduction.dict import lerListadeLinguagens, atualizarListadeLinguagens
from subprocess import Popen
from win10toast_click import ToastNotifier


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        #######################################
        #Configurações da GUI
        #######################################
        self.setupUi(self)
        self.setWindowTitle("TransPy - Tradutor de PDF")
        self.setWindowIcon(QIcon("./icon/arquivo-python-by-Muhammed-Ali.ico")) 
        self.dict = lerListadeLinguagens()
        
        #Repete a tentativa de leitura do arquivo JSON
        try: 
            self.keysDict = list(self.dict.keys())   # type: ignore
        except:  
            while True:
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
        
        #######################################
        #Ações do menu
        #######################################
        self.actionBaixar_novo_pacote_de_l_nguas.triggered.connect(self.actBaixarPacoteDeLinguas)            # type: ignore
        self.actionAbrir_pasta_dos_arquivos.triggered.connect(self.actAbrirPastaArquivos)                     # type: ignore
        
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
        
        textoLido = self.enTextoPDF.toPlainText()
                
        traducao = traduzir(texto=textoLido , linguaSelecionada= self.dict[linguaSelecionada])   # type: ignore
        
        self.enTextoTraduzido.setText(QCoreApplication.translate("MainWindow", traducao, None))
        
    def copiarTextoPDF(self):
        textoPDF = self.enTextoPDF.toPlainText()
        clip.copy(textoPDF)
            
    def copiarTextoTraduzido(self):
        textoTraduzido = self.enTextoTraduzido.toPlainText()
        clip.copy(textoTraduzido)    
    
    def actAbrirPastaArquivos(self):
        path = os.getcwd() + "/files"
        path = os.path.realpath(path)
        
        self.notificacao("Abrindo o diretório!")
        
        Popen(f'explorer "{path}"') 
    
    def actSalvarPesquisa(self):
        pass
    
    def actBaixarPacoteDeLinguas(self):
        #Atualiza a lista de linguagens suportadas pela biblioteca
        atualizarListadeLinguagens()
        
        self.cbLingua.clear()
        
        lerListadeLinguagens()
        
        self.cbLingua.addItem("Default (English)") 
        self.cbLingua.addItems(self.keysDict)
    
    def actSobreOSoftware(self):
        pass
    
    def actComoUsarOSoftware(self):
        pass
    
    def actContatoComOSuporte(self):
        pass
    
    def notificacao(self, mensagem):
        notificação = ToastNotifier()
        
        notificação.show_toast(
            title="TransPy",
            msg=mensagem,
            icon_path= os.getcwd() + "/icon/arquivo-python-by-Muhammed-Ali.ico", 
            duration= 5, threaded=True,
            callback_on_click= None
        )
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
