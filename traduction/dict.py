import imp
import json
from operator import index
import os
from time import sleep
from googletrans import Translator
from googletrans import LANGUAGES
from win10toast_click import ToastNotifier


def atualizarListadeLinguagens():
    ling = LANGUAGES
    
    KEYS = list(ling.keys())
    VALUES = list(ling.values())  
    
    langs = {}
    
    notification = ToastNotifier()
    
    notification.show_toast(
        "TransPy",
        "Baixando as linguagens de programação",
        threaded=True,
        callback_on_click=None,
        duration=10
    )

    for index in range(len(VALUES)):
        value = VALUES[index]
        key = KEYS[index]
        
        tradutor = Translator()
        
        valueTraduct = tradutor.translate(value,dest=key).text     # type: ignore
        
        value = f"{str(value).capitalize()} ({valueTraduct})"
        
        langs[value] = key
    
    with open(os.getcwd() + "/traduction/languagestotraduction.json", "w") as file:
        json.dump(langs,file, indent=3)
        
    sleep(3)
    
    notification.show_toast(
        "TransPy",
        "Todas as línguas baixadas com sucesso!",
        threaded=True,
        callback_on_click=None,
        duration=10)
        

def lerListadeLinguagens():
    try:
        with open(os.getcwd() + "/traduction/languagestotraduction.json", "r") as file:
            langs =json.load(file)
    except:
        langs = atualizarListadeLinguagens()
       
    return langs