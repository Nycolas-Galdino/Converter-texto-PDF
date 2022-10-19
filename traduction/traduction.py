import PyPDF2  
import os
from googletrans import Translator

def traduzir(arquivo, linguaSelecionada = "en"):
    try:
        dir = os.getcwd() + "/files"
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
    except:
        pass

    with open(arquivo, 'rb') as pdfFileObj:
        
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)   
            
        for i in range(pdfReader.numPages):
            
            pageObj = pdfReader.getPage(i)  
                
            pageText = str(pageObj.extractText()) 
            
            try:
                ptFile = open(os.getcwd() + '/files/pdfFile.txt', "r", encoding="utf-8")
                tempText = ptFile.read() + "\n"
                ptFile.close
            except:
                tempText = ""    
            
            ptFile = open(os.getcwd() + f'/files/pdfFile.txt', "w", encoding="utf-8")
            ptFile.write(tempText + pageText)
            ptFile.close
        
        ptFile = open(os.getcwd() + '/files/pdfFile.txt', "r", encoding="utf-8")
        texto = ptFile.read()
        ptFile.close
            
        tradutor = Translator(service_urls=['translate.googleapis.com'])
        
        textoTraduzido = tradutor.translate(texto, dest=linguaSelecionada)
                
        tempFile = open(os.getcwd() + f'/files/{linguaSelecionada}File.txt', "w", encoding="utf-8")
        tempFile.write(textoTraduzido.text)
        tempFile.close
        
        return textoTraduzido.text