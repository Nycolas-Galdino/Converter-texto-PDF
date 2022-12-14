# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QAction, QFont, QIcon)
from PySide6.QtWidgets import (QAbstractScrollArea, QComboBox, QFrame,
    QHBoxLayout, QLabel, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 480)
        MainWindow.setMinimumSize(QSize(630, 480))
        icon = QIcon()
        icon.addFile(u"../icon/arquivo-python-by-Muhammed-Ali.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMenuBar {\n"
"border-bottom:1px solid black;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.actionBaixar_novo_pacote_de_linguas = QAction(MainWindow)
        self.actionBaixar_novo_pacote_de_linguas.setObjectName(u"actionBaixar_novo_pacote_de_linguas")
        self.actionAbrir_pasta_dos_arquivos = QAction(MainWindow)
        self.actionAbrir_pasta_dos_arquivos.setObjectName(u"actionAbrir_pasta_dos_arquivos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame{\n"
"border: 1px solid black;}\n"
"\n"
"QLabel{\n"
"border: none;\n"
"background-color: white\n"
"}\n"
"\n"
"QPushButton, QComboBox {\n"
"padding: 6px;\n"
"border: 1px solid black;\n"
"background-color: white }\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(235,235,235)\n"
"}\n"
"\n"
"QMenuBar{\n"
"background-color:white\n"
"}\n"
"\n"
"*{background-color: lightgrey }")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"QFrame{\n"
"border: none\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnProcurarArquivo = QPushButton(self.frame)
        self.btnProcurarArquivo.setObjectName(u"btnProcurarArquivo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnProcurarArquivo.sizePolicy().hasHeightForWidth())
        self.btnProcurarArquivo.setSizePolicy(sizePolicy)
        self.btnProcurarArquivo.setFont(font)

        self.horizontalLayout_2.addWidget(self.btnProcurarArquivo)

        self.lblNomeDoArquivo = QLabel(self.frame)
        self.lblNomeDoArquivo.setObjectName(u"lblNomeDoArquivo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblNomeDoArquivo.sizePolicy().hasHeightForWidth())
        self.lblNomeDoArquivo.setSizePolicy(sizePolicy1)
        self.lblNomeDoArquivo.setFont(font)
        self.lblNomeDoArquivo.setStyleSheet(u"border: 1px solid black")
        self.lblNomeDoArquivo.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.lblNomeDoArquivo)

        self.cbLingua = QComboBox(self.frame)
        self.cbLingua.addItem("")
        self.cbLingua.setObjectName(u"cbLingua")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbLingua.sizePolicy().hasHeightForWidth())
        self.cbLingua.setSizePolicy(sizePolicy2)
        self.cbLingua.setFont(font)
        self.cbLingua.setAutoFillBackground(False)
        self.cbLingua.setCurrentText(u"Default (English)")
        self.cbLingua.setMaxVisibleItems(150)
        self.cbLingua.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.cbLingua.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_2.addWidget(self.cbLingua)


        self.verticalLayout_4.addWidget(self.frame)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet(u"QFrame{\n"
"background-color: white\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 281, 260))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.enTextoPDF = QTextEdit(self.scrollAreaWidgetContents)
        self.enTextoPDF.setObjectName(u"enTextoPDF")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.enTextoPDF.sizePolicy().hasHeightForWidth())
        self.enTextoPDF.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setBold(False)
        self.enTextoPDF.setFont(font1)
        self.enTextoPDF.setStyleSheet(u"border:none")
        self.enTextoPDF.setAutoFormatting(QTextEdit.AutoAll)
        self.enTextoPDF.setOverwriteMode(True)
        self.enTextoPDF.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.enTextoPDF)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.btnCopiarTextoPDF = QPushButton(self.widget_2)
        self.btnCopiarTextoPDF.setObjectName(u"btnCopiarTextoPDF")
        self.btnCopiarTextoPDF.setFont(font)

        self.verticalLayout.addWidget(self.btnCopiarTextoPDF)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea_2 = QScrollArea(self.widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 281, 260))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.enTextoTraduzido = QTextEdit(self.scrollAreaWidgetContents_2)
        self.enTextoTraduzido.setObjectName(u"enTextoTraduzido")
        self.enTextoTraduzido.setStyleSheet(u"border:none")
        self.enTextoTraduzido.setAutoFormatting(QTextEdit.AutoAll)
        self.enTextoTraduzido.setOverwriteMode(True)
        self.enTextoTraduzido.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_6.addWidget(self.enTextoTraduzido)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.scrollArea_2)

        self.btnCopiarTextoTraduzido = QPushButton(self.widget)
        self.btnCopiarTextoTraduzido.setObjectName(u"btnCopiarTextoTraduzido")
        self.btnCopiarTextoTraduzido.setFont(font)

        self.verticalLayout_2.addWidget(self.btnCopiarTextoTraduzido)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.btnTraduzir = QPushButton(self.centralwidget)
        self.btnTraduzir.setObjectName(u"btnTraduzir")
        self.btnTraduzir.setFont(font)
        self.btnTraduzir.setStyleSheet(u"QPushButton:Hover{\n"
"background-color: lightblue\n"
"}")

        self.verticalLayout_3.addWidget(self.btnTraduzir)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.rodape = QLabel(self.centralwidget)
        self.rodape.setObjectName(u"rodape")
        sizePolicy2.setHeightForWidth(self.rodape.sizePolicy().hasHeightForWidth())
        self.rodape.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(6)
        font2.setBold(True)
        self.rodape.setFont(font2)
        self.rodape.setStyleSheet(u"QLabel{\n"
"background-color: rgba(0,0,0,0);\n"
"}\n"
"\n"
"")
        self.rodape.setTextFormat(Qt.AutoText)
        self.rodape.setOpenExternalLinks(True)
        self.rodape.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout_5.addWidget(self.rodape)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 630, 22))
        self.menuArquivo = QMenu(self.menuBar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        self.menuOp_es = QMenu(self.menuBar)
        self.menuOp_es.setObjectName(u"menuOp_es")
        MainWindow.setMenuBar(self.menuBar)
#if QT_CONFIG(shortcut)
        self.lblNomeDoArquivo.setBuddy(self.cbLingua)
#endif // QT_CONFIG(shortcut)

        self.menuBar.addAction(self.menuArquivo.menuAction())
        self.menuBar.addAction(self.menuOp_es.menuAction())
        self.menuArquivo.addAction(self.actionAbrir_pasta_dos_arquivos)
        self.menuOp_es.addAction(self.actionBaixar_novo_pacote_de_linguas)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TransPy - Tradutor de PDF", None))
        self.actionBaixar_novo_pacote_de_linguas.setText(QCoreApplication.translate("MainWindow", u"Baixar novo pacote de l\u00ednguas.", None))
#if QT_CONFIG(shortcut)
        self.actionBaixar_novo_pacote_de_linguas.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir_pasta_dos_arquivos.setText(QCoreApplication.translate("MainWindow", u"Abrir pasta dos arquivos", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir_pasta_dos_arquivos.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+A", None))
#endif // QT_CONFIG(shortcut)
        self.btnProcurarArquivo.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivo", None))
        self.lblNomeDoArquivo.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
        self.cbLingua.setItemText(0, QCoreApplication.translate("MainWindow", u"Default (English)", None))

#if QT_CONFIG(tooltip)
        self.cbLingua.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Selecione ao idioma que deseja traduzir.</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.enTextoPDF.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Texto do PDF", None))
        self.btnCopiarTextoPDF.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
        self.enTextoTraduzido.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Texto traduzido", None))
        self.btnCopiarTextoTraduzido.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
        self.btnTraduzir.setText(QCoreApplication.translate("MainWindow", u"Traduzir", None))
        self.rodape.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Desenvolvido por <a href=\"https://github.com/Nycolas-Galdino\" >Nycolas Galdino</a></p></body></html>", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivos", None))
        self.menuOp_es.setTitle(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es", None))
    # retranslateUi

