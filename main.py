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
    def __init__(self) -> None: #Configurações iniciais/globais do projeto
        super(MainWindow, self).__init__()
        
        #######################################
        #Configurações da GUI
        #######################################
        self.setupUi(self)
        self.setWindowTitle("TransPy - Tradutor de PDF")
        self.setWindowIcon(QIcon("./icon/arquivo-python-icon-by-Muhammed-Ali.ico")) 
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
        self.actionBaixar_novo_pacote_de_linguas.triggered.connect(self.actBaixarPacoteDeLinguas)   
        self.actionAbrir_pasta_dos_arquivos.triggered.connect(self.actAbrirPastaArquivos)    
        
        #######################################
        #Cria uma pasta chamado files ao abrir o software
        #######################################
        try:
            os.mkdir(os.getcwd() + "/files")
        except:
            pass 
        
    def procurarArquivo(self): #Abre o explorer e seleciona o arquivo a traduzir
        
        #Seleciona o arquivo e coloca seu nome nome na tela
        self.arquivo = QFileDialog.getOpenFileName(self, "Open PDF", os.getcwd(), "PDF Files (*.pdf)" )[0]
        self.lblNomeDoArquivo.setText(QCoreApplication.translate("MainWindow", self.arquivo, None))
       
        lerArquivo(arquivo=self.arquivo)
        
        #Coleta o texto escrito no arquivo pdfFile.txt e o salva em uma variável
        with open(os.getcwd() + '/files/pdfFile.txt', "r", encoding="utf-8") as pdfFile:
            texto = pdfFile.read()
        
        #Adiciona o texto lido dentro da tela
        self.enTextoPDF.setText(QCoreApplication.translate("MainWindow", texto, None))
    
    def traduzirTXT(self): #Traduz o arquivo lido
        #Lê a lingua selecionada para traduzir
        linguaSelecionada = self.cbLingua.currentText()
        try:
            if linguaSelecionada == "Default (English)": #Caso não selecione nenhuma língua, irá traduzir para uma linguagem padrão 
                linguaSelecionada = "English (english)"
            
            self.notificacao(mensagem="Traduzindo o texto para " + linguaSelecionada)
            
            #Lê o texto original e o traduzir para a linguagem selecionada
            textoLido = self.enTextoPDF.toPlainText()
            traducao = traduzir(texto=textoLido , linguaSelecionada= self.dict[linguaSelecionada])   # type: ignore
            
            self.enTextoTraduzido.setText(QCoreApplication.translate("MainWindow", traducao, None))
        except:
            self.notificacao(mensagem="Erro ao traduzir o texto.") #Notifica caso aja erro durante o processo
        
    def copiarTextoPDF(self): #Copia o texto original
        textoPDF = self.enTextoPDF.toPlainText()
        clip.copy(textoPDF)
            
    def copiarTextoTraduzido(self): #Copia o texto traduzido
        textoTraduzido = self.enTextoTraduzido.toPlainText()
        clip.copy(textoTraduzido)    
    
    def actAbrirPastaArquivos(self): #Abre a pasta onde está salvo os arquivos
        path = os.getcwd() + "/files"
        path = os.path.realpath(path)
        
        self.notificacao("Abrindo o diretório!")
        
        Popen(f'explorer "{path}"') 
        
    def actBaixarPacoteDeLinguas(self): #Atualiza a lista de linguagens suportadas pela biblioteca
        atualizarListadeLinguagens()
        
        self.cbLingua.clear()
        
        lerListadeLinguagens()
        
        self.cbLingua.addItem("Default (English)") 
        self.cbLingua.addItems(self.keysDict)
    
    def notificacao(self, mensagem): #Envia uma notificação com base nos critérios selecionados
        notificação = ToastNotifier()
        
        notificação.show_toast(
            title="TransPy",
            msg=mensagem,
            icon_path= os.getcwd() + "/icon/arquivo-python-icon-by-Muhammed-Ali.ico", 
            duration= 5, threaded=True,
            callback_on_click= None
        )
    
if __name__ == "__main__":  #Inicia o projeto
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
