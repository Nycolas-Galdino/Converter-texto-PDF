import PyPDF2  
import os
from googletrans import Translator

try:
    os.remove(os.getcwd() + '/ptFile.txt')
except:
    pass


with open(os.getcwd() + '/Catálogo Trurium 2022.pdf', 'rb') as pdfFileObj:
     
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
        
    print(pdfReader.numPages)  
        
    for i in range(pdfReader.numPages):
        print(f"Página {i}: \n")

        pageObj = pdfReader.getPage(i)  
            
        pageText = str(pageObj.extractText()) 
        
        try:
            ptFile = open(os.getcwd() + '/ptFile.txt', "r", encoding="utf-8")
            tempText = ptFile.read() + "\n"
            ptFile.close
        except:
            tempText = ""    
        
        ptFile = open(os.getcwd() + '/ptFile.txt', "w", encoding="utf-8")
        ptFile.write(tempText + pageText)
        ptFile.close
    
    ptFile = open(os.getcwd() + '/ptFile.txt', "r", encoding="utf-8")
    texto = ptFile.read()
    ptFile.close
        
    tradutor = Translator(service_urls=['translate.googleapis.com'])
    
    textoTraduzido = tradutor.translate(texto, dest='en')
    
    print(textoTraduzido.text)
    
    enFile = open(os.getcwd() + '/enFile.txt', "w", encoding="utf-8")
    enFile.write(textoTraduzido.text)
    enFile.close