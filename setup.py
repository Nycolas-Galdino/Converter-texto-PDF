import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.

listFiles = ['README.md', 'screens/ui_mainwindow.py', 'traduction/dict.py', 
                                   'traduction/languagestotraduction.json','traduction/traduction.py']

build_options = {'packages': [], 'excludes': ['tkinter'],'include_files': listFiles,'optimize': 2, 'replace_paths': [("*", "")]}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'TransPy')
]

setup(name='TransPy - Tradutor de PDF',
      version = '1.4',
      description = 'TransPy é um software cujo objetivo é ler e traduzir um PDF utilizando a linguagem Python como base.',
      options = {'build_exe': build_options},
      executables = executables)

def copy(arquivo):
    copyFile = os.getcwd() + arquivo

def past(arquivo):
    pass

for file in listFiles:
    pass
