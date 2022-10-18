# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollBar,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(796, 459)
        MainWindow.setMinimumSize(QSize(460, 318))
        MainWindow.setStyleSheet(u"QFrame{\n"
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
"*{\n"
"background-color: lightgray}")
        self.actionAcessar_pasta_atual = QAction(MainWindow)
        self.actionAcessar_pasta_atual.setObjectName(u"actionAcessar_pasta_atual")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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
        self.cbLingua.addItem("")
        self.cbLingua.addItem("")
        self.cbLingua.addItem("")
        self.cbLingua.addItem("")
        self.cbLingua.setObjectName(u"cbLingua")
        sizePolicy.setHeightForWidth(self.cbLingua.sizePolicy().hasHeightForWidth())
        self.cbLingua.setSizePolicy(sizePolicy)
        self.cbLingua.setFont(font)
        self.cbLingua.setInsertPolicy(QComboBox.InsertAlphabetically)

        self.horizontalLayout_2.addWidget(self.cbLingua)


        self.verticalLayout_3.addWidget(self.frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet(u"QFrame{\n"
"background-color: white\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.widget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.lblTextoPDF = QLabel(self.frame_2)
        self.lblTextoPDF.setObjectName(u"lblTextoPDF")
        sizePolicy.setHeightForWidth(self.lblTextoPDF.sizePolicy().hasHeightForWidth())
        self.lblTextoPDF.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(False)
        self.lblTextoPDF.setFont(font1)
        self.lblTextoPDF.setStyleSheet(u"padding: 2%")
        self.lblTextoPDF.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblTextoPDF.setWordWrap(True)
        self.lblTextoPDF.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.lblTextoPDF)

        self.vcbTextoPDF = QScrollBar(self.frame_2)
        self.vcbTextoPDF.setObjectName(u"vcbTextoPDF")
        self.vcbTextoPDF.setFont(font)
        self.vcbTextoPDF.setOrientation(Qt.Vertical)

        self.horizontalLayout_3.addWidget(self.vcbTextoPDF)


        self.verticalLayout.addWidget(self.frame_2)

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
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color: white;\n"
"}\n"
"\n"
"QScrollBar {\n"
"position: fixed;\n"
"right: 2\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.lblTextoTraduzido = QLabel(self.frame_3)
        self.lblTextoTraduzido.setObjectName(u"lblTextoTraduzido")
        self.lblTextoTraduzido.setFont(font1)
        self.lblTextoTraduzido.setStyleSheet(u"padding: 2%")
        self.lblTextoTraduzido.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lblTextoTraduzido.setWordWrap(True)
        self.lblTextoTraduzido.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_4.addWidget(self.lblTextoTraduzido)

        self.vcbTextoTraduzido = QScrollBar(self.frame_3)
        self.vcbTextoTraduzido.setObjectName(u"vcbTextoTraduzido")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.vcbTextoTraduzido.sizePolicy().hasHeightForWidth())
        self.vcbTextoTraduzido.setSizePolicy(sizePolicy3)
        self.vcbTextoTraduzido.setFont(font)
        self.vcbTextoTraduzido.setOrientation(Qt.Vertical)

        self.horizontalLayout_4.addWidget(self.vcbTextoTraduzido)


        self.verticalLayout_2.addWidget(self.frame_3)

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

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAcessar_pasta_atual.setText(QCoreApplication.translate("MainWindow", u"Acessar pasta atual", None))
        self.btnProcurarArquivo.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivo", None))
        self.lblNomeDoArquivo.setText(QCoreApplication.translate("MainWindow", u"Nome do arquivo", None))
        self.cbLingua.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.cbLingua.setItemText(1, QCoreApplication.translate("MainWindow", u"en", None))
        self.cbLingua.setItemText(2, QCoreApplication.translate("MainWindow", u"pt-br", None))
        self.cbLingua.setItemText(3, QCoreApplication.translate("MainWindow", u"de", None))
        self.cbLingua.setItemText(4, QCoreApplication.translate("MainWindow", u"es", None))

#if QT_CONFIG(tooltip)
        self.cbLingua.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Selecione ao idioma que deseja traduzir.</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cbLingua.setCurrentText(QCoreApplication.translate("MainWindow", u"Selecione", None))
        self.lblTextoPDF.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Texto do PDF</p></body></html>", None))
        self.btnCopiarTextoPDF.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
        self.lblTextoTraduzido.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Texto traduzido</p></body></html>", None))
        self.btnCopiarTextoTraduzido.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
        self.btnTraduzir.setText(QCoreApplication.translate("MainWindow", u"Traduzir", None))
    # retranslateUi

