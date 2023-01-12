import os
from cx_Freeze import setup, Executable
import sys

listFiles = ['README.md', 
             'screens/ui_mainwindow.py',
             'traduction/dict.py',
             'traduction/languagestotraduction.json','traduction/traduction.py', ]

build_options = {'packages': [], 'excludes': ['tkinter'],'include_files': listFiles,'optimize': 2, 'replace_paths': [("*", "")]}

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py',
               base = base,
               target_name = 'TransPy',
               icon = 'icon/arquivo-python-icon-by-Muhammed-Ali.ico'
               )
]

setup(name='TransPy - Tradutor de PDF',
      version = '2.2',
      description = 'TransPy é um software cujo objetivo é ler e traduzir um PDF utilizando a linguagem Python como base.',
      options = {'build_exe': build_options},
      executables = executables)
