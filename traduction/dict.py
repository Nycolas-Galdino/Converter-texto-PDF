import json
from operator import index
import os
from googletrans import Translator
from googletrans import LANGUAGES


def atualizarListadeLinguagens():
    ling = LANGUAGES
    
    KEYS = list(ling.keys())
    VALUES = list(ling.values())  
    
    langs = {}

    for index in range(len(VALUES)):
        value = VALUES[index]
        key = KEYS[index]
        
        tradutor = Translator()
        
        valueTraduct = tradutor.translate(value,dest=key).text
        
        value = f"{str(value).capitalize()} ({valueTraduct})"
        
        langs[value] = key
        
        print(value , " - ", key)
        
    
    with open(os.getcwd() + "/traduction/languagestotraduction.json", "w") as file:
        json.dump(langs,file, indent=3)
        

def lerListadeLinguagens():
    with open(os.getcwd() + "/traduction/languagestotraduction.json", "r") as file:
        try:
            langs =json.load(file)
            print("Arquivo Langs lido com sucesso")
        except:
            langs = atualizarListadeLinguagens()
        
    return langs