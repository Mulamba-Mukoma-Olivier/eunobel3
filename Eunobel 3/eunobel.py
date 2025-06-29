from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(874, 566)
        MainWindow.setStyleSheet(u"background: #1c1c1c;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0,0,0,0)
        self.horizontalLayout.setSpacing(0)
        
        self.mainPage = QWidget(self.centralwidget)
        self.mainPage.setObjectName(u"mainPage")
        self.horizontalLayout_2 = QHBoxLayout(self.mainPage)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MainTable = QTabWidget(self.mainPage)
        self.MainTable.setObjectName(u"MainTable")
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.MainTable.setFont(font)
        self.MainTable.setStyleSheet(u"QLabel{\n"
"	color: #fff;\n"
"	font-weight: 900;\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background: #fff;\n"
"	font-weight: 900;\n"
"	color: #333;\n"
"	padding: 10px; \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #4b7bb2;\n"
"	font-weight: 900;\n"
"	color: #fff;\n"
"	padding: 10px; \n"
"}")
        self.produit_page = QWidget()
        self.produit_page.setObjectName(u"produit_page")
        
        self.horizontalLayout_3 = QHBoxLayout(self.produit_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0,0,0,0)
        self.horizontalLayout_3.setSpacing(0)
        
        self.widget = QWidget(self.produit_page)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.table_produit = QTableWidget(self.widget)
        if (self.table_produit.columnCount() < 7):
            self.table_produit.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_produit.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_produit.setObjectName(u"table_produit")

        self.horizontalLayout_5.addWidget(self.table_produit)


        self.horizontalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.produit_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(150, 16777215))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0,0,0,0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalSpacer = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.supprimer_produit_btn = QPushButton(self.widget_2)
        self.supprimer_produit_btn.setObjectName(u"supprimer_produit_btn")

        self.verticalLayout.addWidget(self.supprimer_produit_btn)

        self.actualiser_produit_btn = QPushButton(self.widget_2)
        self.actualiser_produit_btn.setObjectName(u"actualiser_produit_btn")

        self.verticalLayout.addWidget(self.actualiser_produit_btn)

        self.verticalSpacer = QSpacerItem(20, 570, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.widget_2)

        self.MainTable.addTab(self.produit_page, "")
        self.page_client = QWidget()
        self.page_client.setObjectName(u"page_client")
        self.horizontalLayout_8 = QHBoxLayout(self.page_client)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0,0,0,0)
        self.horizontalLayout_8.setSpacing(0)
        
        self.client_main_page = QWidget(self.page_client)
        self.client_main_page.setObjectName(u"client_main_page")
        self.horizontalLayout_6 = QHBoxLayout(self.client_main_page)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.table_client = QTableWidget(self.client_main_page)
        if (self.table_client.columnCount() < 4):
            self.table_client.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_client.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.table_client.setObjectName(u"table_client")

        self.horizontalLayout_6.addWidget(self.table_client)


        self.horizontalLayout_8.addWidget(self.client_main_page)

        self.widget_4 = QWidget(self.page_client)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0,0,0,0)
        self.horizontalLayout_7.setSpacing(0)
        
        self.horizontalSpacer_3 = QSpacerItem(28, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.supprimer_client_btn = QPushButton(self.widget_4)
        self.supprimer_client_btn.setObjectName(u"supprimer_client_btn")

        self.verticalLayout_2.addWidget(self.supprimer_client_btn)

        self.actualiser_client_btn = QPushButton(self.widget_4)
        self.actualiser_client_btn.setObjectName(u"actualiser_client_btn")

        self.verticalLayout_2.addWidget(self.actualiser_client_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 438, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addWidget(self.widget_4)

        self.MainTable.addTab(self.page_client, "")
        self.page_stocks = QWidget()
        self.page_stocks.setObjectName(u"page_stocks")
        self.horizontalLayout_33 = QHBoxLayout(self.page_stocks)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0,0,0,0)
        self.horizontalLayout_33.setSpacing(0)
        
        self.stocks_main_page = QWidget(self.page_stocks)
        self.stocks_main_page.setObjectName(u"stocks_main_page")
        self.horizontalLayout_9 = QHBoxLayout(self.stocks_main_page)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        
        self.table_stocks = QTableWidget(self.stocks_main_page)
        if (self.table_stocks.columnCount() < 3):
            self.table_stocks.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_stocks.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_stocks.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_stocks.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        self.table_stocks.setObjectName(u"table_stocks")

        self.horizontalLayout_9.addWidget(self.table_stocks)


        self.horizontalLayout_33.addWidget(self.stocks_main_page)

        self.widget_6 = QWidget(self.page_stocks)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(150, 0))
        self.widget_6.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setContentsMargins(0,0,0,0)
        self.verticalLayout_3.setSpacing(0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_10.addWidget(self.label_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.supprimer_stocks_btn = QPushButton(self.widget_6)
        self.supprimer_stocks_btn.setObjectName(u"supprimer_stocks_btn")

        self.verticalLayout_3.addWidget(self.supprimer_stocks_btn)

        self.actualiser_stocks_btn = QPushButton(self.widget_6)
        self.actualiser_stocks_btn.setObjectName(u"actualiser_stocks_btn")

        self.verticalLayout_3.addWidget(self.actualiser_stocks_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 570, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_33.addWidget(self.widget_6)

        self.MainTable.addTab(self.page_stocks, "")
        self.page_fournisseur = QWidget()
        self.page_fournisseur.setObjectName(u"page_fournisseur")
        self.horizontalLayout_34 = QHBoxLayout(self.page_fournisseur)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setContentsMargins(0,0,0,0)
        
        self.fournisseur_main_page = QWidget(self.page_fournisseur)
        self.fournisseur_main_page.setObjectName(u"fournisseur_main_page")
        
        self.horizontalLayout_20 = QHBoxLayout(self.fournisseur_main_page)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        
        self.table_fournisseur = QTableWidget(self.fournisseur_main_page)
        if (self.table_fournisseur.columnCount() < 4):
            self.table_fournisseur.setColumnCount(4)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_fournisseur.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_fournisseur.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_fournisseur.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_fournisseur.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        self.table_fournisseur.setObjectName(u"table_fournisseur")

        self.horizontalLayout_20.addWidget(self.table_fournisseur)


        self.horizontalLayout_34.addWidget(self.fournisseur_main_page)

        self.widget_13 = QWidget(self.page_fournisseur)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(150, 0))
        self.widget_13.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.widget_13)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_13)

        self.label_7 = QLabel(self.widget_13)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_19.addWidget(self.label_7)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_14)


        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.supprimer_fournisseur_btn = QPushButton(self.widget_13)
        self.supprimer_fournisseur_btn.setObjectName(u"supprimer_fournisseur_btn")

        self.verticalLayout_7.addWidget(self.supprimer_fournisseur_btn)

        self.actualiser_fournisseur_btn = QPushButton(self.widget_13)
        self.actualiser_fournisseur_btn.setObjectName(u"actualiser_fournisseur_btn")

        self.verticalLayout_7.addWidget(self.actualiser_fournisseur_btn)

        self.verticalSpacer_7 = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.horizontalLayout_34.addWidget(self.widget_13)

        self.MainTable.addTab(self.page_fournisseur, "")
        self.page_entrepot = QWidget()
        self.page_entrepot.setObjectName(u"page_entrepot")
        self.horizontalLayout_35 = QHBoxLayout(self.page_entrepot)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.entrepots_main_page = QWidget(self.page_entrepot)
        self.entrepots_main_page.setObjectName(u"entrepots_main_page")
        self.horizontalLayout_22 = QHBoxLayout(self.entrepots_main_page)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.table_entrepot = QTableWidget(self.entrepots_main_page)
        if (self.table_entrepot.columnCount() < 2):
            self.table_entrepot.setColumnCount(2)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_entrepot.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_entrepot.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        self.table_entrepot.setObjectName(u"table_entrepot")

        self.horizontalLayout_22.addWidget(self.table_entrepot)


        self.horizontalLayout_35.addWidget(self.entrepots_main_page)

        self.widget_15 = QWidget(self.page_entrepot)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(150, 0))
        self.widget_15.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.widget_15)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_15)

        self.label_8 = QLabel(self.widget_15)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_21.addWidget(self.label_8)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_16)


        self.verticalLayout_8.addLayout(self.horizontalLayout_21)

        self.supprimer_entrepots_btn = QPushButton(self.widget_15)
        self.supprimer_entrepots_btn.setObjectName(u"supprimer_entrepots_btn")

        self.verticalLayout_8.addWidget(self.supprimer_entrepots_btn)

        self.actualiser_entrepots_btn = QPushButton(self.widget_15)
        self.actualiser_entrepots_btn.setObjectName(u"actualiser_entrepots_btn")

        self.verticalLayout_8.addWidget(self.actualiser_entrepots_btn)

        self.verticalSpacer_8 = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_8)


        self.horizontalLayout_35.addWidget(self.widget_15)

        self.MainTable.addTab(self.page_entrepot, "")
        self.page_entrees = QWidget()
        self.page_entrees.setObjectName(u"page_entrees")
        self.horizontalLayout_36 = QHBoxLayout(self.page_entrees)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.entrees_main_page = QWidget(self.page_entrees)
        self.entrees_main_page.setObjectName(u"entrees_main_page")
        self.horizontalLayout_24 = QHBoxLayout(self.entrees_main_page)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.table_entrees = QTableWidget(self.entrees_main_page)
        if (self.table_entrees.columnCount() < 5):
            self.table_entrees.setColumnCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_entrees.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_entrees.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_entrees.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_entrees.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_entrees.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        self.table_entrees.setObjectName(u"table_entrees")

        self.horizontalLayout_24.addWidget(self.table_entrees)


        self.horizontalLayout_36.addWidget(self.entrees_main_page)

        self.widget_17 = QWidget(self.page_entrees)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(150, 0))
        self.widget_17.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.widget_17)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_17)

        self.label_9 = QLabel(self.widget_17)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_23.addWidget(self.label_9)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_18)


        self.verticalLayout_9.addLayout(self.horizontalLayout_23)

        self.supprimer_entrees_btn = QPushButton(self.widget_17)
        self.supprimer_entrees_btn.setObjectName(u"supprimer_entrees_btn")

        self.verticalLayout_9.addWidget(self.supprimer_entrees_btn)

        self.actualiser_entrees_btn = QPushButton(self.widget_17)
        self.actualiser_entrees_btn.setObjectName(u"actualiser_entrees_btn")

        self.verticalLayout_9.addWidget(self.actualiser_entrees_btn)

        self.verticalSpacer_9 = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_9)


        self.horizontalLayout_36.addWidget(self.widget_17)

        self.MainTable.addTab(self.page_entrees, "")
        self.page_sorties = QWidget()
        self.page_sorties.setObjectName(u"page_sorties")
        self.horizontalLayout_37 = QHBoxLayout(self.page_sorties)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.sorties_main_page = QWidget(self.page_sorties)
        self.sorties_main_page.setObjectName(u"sorties_main_page")
        self.horizontalLayout_26 = QHBoxLayout(self.sorties_main_page)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.table_sorties = QTableWidget(self.sorties_main_page)
        if (self.table_sorties.columnCount() < 5):
            self.table_sorties.setColumnCount(5)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_sorties.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_sorties.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_sorties.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_sorties.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_sorties.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        self.table_sorties.setObjectName(u"table_sorties")

        self.horizontalLayout_26.addWidget(self.table_sorties)


        self.horizontalLayout_37.addWidget(self.sorties_main_page)

        self.widget_19 = QWidget(self.page_sorties)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(150, 0))
        self.widget_19.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.widget_19)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_19)

        self.label_10 = QLabel(self.widget_19)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_25.addWidget(self.label_10)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_20)


        self.verticalLayout_10.addLayout(self.horizontalLayout_25)

        self.supprimer_sorties_btn = QPushButton(self.widget_19)
        self.supprimer_sorties_btn.setObjectName(u"supprimer_sorties_btn")

        self.verticalLayout_10.addWidget(self.supprimer_sorties_btn)

        self.actualiser_sorties_btn = QPushButton(self.widget_19)
        self.actualiser_sorties_btn.setObjectName(u"actualiser_sorties_btn")

        self.verticalLayout_10.addWidget(self.actualiser_sorties_btn)

        self.verticalSpacer_10 = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_10)


        self.horizontalLayout_37.addWidget(self.widget_19)

        self.MainTable.addTab(self.page_sorties, "")
        self.page_c_fournisseur = QWidget()
        self.page_c_fournisseur.setObjectName(u"page_c_fournisseur")
        self.horizontalLayout_38 = QHBoxLayout(self.page_c_fournisseur)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.commande_f_main_page = QWidget(self.page_c_fournisseur)
        self.commande_f_main_page.setObjectName(u"commande_f_main_page")
        self.horizontalLayout_28 = QHBoxLayout(self.commande_f_main_page)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.table_commande_f = QTableWidget(self.commande_f_main_page)
        if (self.table_commande_f.columnCount() < 3):
            self.table_commande_f.setColumnCount(3)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_commande_f.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_commande_f.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_commande_f.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        self.table_commande_f.setObjectName(u"table_commande_f")

        self.horizontalLayout_28.addWidget(self.table_commande_f)


        self.horizontalLayout_38.addWidget(self.commande_f_main_page)

        self.widget_21 = QWidget(self.page_c_fournisseur)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(150, 0))
        self.widget_21.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.widget_21)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_21)

        self.label_11 = QLabel(self.widget_21)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_27.addWidget(self.label_11)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_22)


        self.verticalLayout_11.addLayout(self.horizontalLayout_27)

        self.supprimer_cf_btn = QPushButton(self.widget_21)
        self.supprimer_cf_btn.setObjectName(u"supprimer_cf_btn")

        self.verticalLayout_11.addWidget(self.supprimer_cf_btn)

        self.actualiser_cf_btn = QPushButton(self.widget_21)
        self.actualiser_cf_btn.setObjectName(u"actualiser_cf_btn")

        self.verticalLayout_11.addWidget(self.actualiser_cf_btn)

        self.verticalSpacer_11 = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_11)


        self.horizontalLayout_38.addWidget(self.widget_21)

        self.MainTable.addTab(self.page_c_fournisseur, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_39 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.commande_c_main_page = QWidget(self.tab_2)
        self.commande_c_main_page.setObjectName(u"commande_c_main_page")
        self.horizontalLayout_30 = QHBoxLayout(self.commande_c_main_page)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.table_commande_c = QTableWidget(self.commande_c_main_page)
        if (self.table_commande_c.columnCount() < 3):
            self.table_commande_c.setColumnCount(3)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_commande_c.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_commande_c.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_commande_c.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        self.table_commande_c.setObjectName(u"table_commande_c")

        self.horizontalLayout_30.addWidget(self.table_commande_c)


        self.horizontalLayout_39.addWidget(self.commande_c_main_page)

        self.widget_23 = QWidget(self.tab_2)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(150, 0))
        self.widget_23.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.widget_23)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_23)

        self.label_12 = QLabel(self.widget_23)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_29.addWidget(self.label_12)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_24)


        self.verticalLayout_12.addLayout(self.horizontalLayout_29)

        self.supprimer_cc_btn = QPushButton(self.widget_23)
        self.supprimer_cc_btn.setObjectName(u"supprimer_cc_btn")

        self.verticalLayout_12.addWidget(self.supprimer_cc_btn)

        self.actualiser_cc_btn = QPushButton(self.widget_23)
        self.actualiser_cc_btn.setObjectName(u"actualiser_cc_btn")

        self.verticalLayout_12.addWidget(self.actualiser_cc_btn)

        self.verticalSpacer_12 = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_12)


        self.horizontalLayout_39.addWidget(self.widget_23)

        self.MainTable.addTab(self.tab_2, "")
        self.page_utilisateur = QWidget()
        self.page_utilisateur.setObjectName(u"page_utilisateur")
        self.horizontalLayout_40 = QHBoxLayout(self.page_utilisateur)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.utilisateur_main_page = QWidget(self.page_utilisateur)
        self.utilisateur_main_page.setObjectName(u"utilisateur_main_page")
        self.horizontalLayout_32 = QHBoxLayout(self.utilisateur_main_page)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.table_produit_11 = QTableWidget(self.utilisateur_main_page)
        if (self.table_produit_11.columnCount() < 2):
            self.table_produit_11.setColumnCount(2)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_produit_11.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_produit_11.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        self.table_produit_11.setObjectName(u"table_produit_11")

        self.horizontalLayout_32.addWidget(self.table_produit_11)


        self.horizontalLayout_40.addWidget(self.utilisateur_main_page)

        self.widget_25 = QWidget(self.page_utilisateur)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMinimumSize(QSize(150, 0))
        self.widget_25.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.widget_25)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_25)

        self.label_13 = QLabel(self.widget_25)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_31.addWidget(self.label_13)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_26)


        self.verticalLayout_13.addLayout(self.horizontalLayout_31)

        self.supprimer_utilisateur_btn = QPushButton(self.widget_25)
        self.supprimer_utilisateur_btn.setObjectName(u"supprimer_utilisateur_btn")

        self.verticalLayout_13.addWidget(self.supprimer_utilisateur_btn)

        self.actualiser_utilisateur_btn = QPushButton(self.widget_25)
        self.actualiser_utilisateur_btn.setObjectName(u"actualiser_utilisateur_btn")

        self.verticalLayout_13.addWidget(self.actualiser_utilisateur_btn)

        self.verticalSpacer_13 = QSpacerItem(20, 368, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_13)


        self.horizontalLayout_40.addWidget(self.widget_25)

        self.MainTable.addTab(self.page_utilisateur, "")
        self.OptionTab = QWidget()
        self.OptionTab.setObjectName(u"OptionTab")
        self.horizontalLayout_41 = QHBoxLayout(self.OptionTab)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.page_supprimer_2 = QTabWidget(self.OptionTab)
        self.page_supprimer_2.setObjectName(u"page_supprimer_2")
        self.page_supprimer_2.setStyleSheet(u"background: #4b7bb2;")
        self.tab_formulaire_produits = QWidget()
        self.tab_formulaire_produits.setObjectName(u"tab_formulaire_produits")
        self.horizontalLayout_46 = QHBoxLayout(self.tab_formulaire_produits)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_15)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_31 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_31)

        self.widget_3 = QWidget(self.tab_formulaire_produits)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(500, 0))
        self.widget_3.setMaximumSize(QSize(500, 16777215))
        self.widget_3.setStyleSheet(u"background: #fff;\n"
"color: #1c1c1c;")
        self.verticalLayout_14 = QVBoxLayout(self.widget_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_29)

        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_44.addWidget(self.label_17)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_30)


        self.verticalLayout_14.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout = QGridLayout(self.widget_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_3 = QLineEdit(self.widget_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 35))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.lineEdit_3, 5, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 35))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)

        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 35))
        self.lineEdit.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.label_14 = QLabel(self.widget_5)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 1)


        self.horizontalLayout_43.addWidget(self.widget_5)

        self.widget_14 = QWidget(self.widget_3)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_2 = QGridLayout(self.widget_14)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_18 = QLabel(self.widget_14)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_2.addWidget(self.label_18, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.widget_14)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 35))
        self.lineEdit_5.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_2.addWidget(self.lineEdit_5, 1, 0, 1, 1)

        self.label_19 = QLabel(self.widget_14)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.widget_14)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 35))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_2.addWidget(self.lineEdit_6, 3, 0, 1, 1)

        self.label_20 = QLabel(self.widget_14)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 4, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widget_14)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 35))
        self.lineEdit_7.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_2.addWidget(self.lineEdit_7, 5, 0, 1, 1)


        self.horizontalLayout_43.addWidget(self.widget_14)


        self.verticalLayout_14.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.save_produit_btn = QPushButton(self.widget_3)
        self.save_produit_btn.setObjectName(u"save_produit_btn")
        self.save_produit_btn.setMinimumSize(QSize(250, 35))
        self.save_produit_btn.setMaximumSize(QSize(250, 35))
        self.save_produit_btn.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;\n"
"font-size: 20px;\n"
"padding: 0;")

        self.horizontalLayout_42.addWidget(self.save_produit_btn)


        self.verticalLayout_14.addLayout(self.horizontalLayout_42)


        self.horizontalLayout_45.addWidget(self.widget_3)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_32)


        self.verticalLayout_15.addLayout(self.horizontalLayout_45)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_14)


        self.horizontalLayout_46.addLayout(self.verticalLayout_15)

        self.page_supprimer_2.addTab(self.tab_formulaire_produits, "")
        self.tab_formulaire_client = QWidget()
        self.tab_formulaire_client.setObjectName(u"tab_formulaire_client")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_formulaire_client)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_16)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalSpacer_33 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_33)

        self.widget_7 = QWidget(self.tab_formulaire_client)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(500, 0))
        self.widget_7.setMaximumSize(QSize(500, 16777215))
        self.widget_7.setStyleSheet(u"background: #fff;\n"
"color: #1c1c1c;")
        self.verticalLayout_17 = QVBoxLayout(self.widget_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_34)

        self.label_21 = QLabel(self.widget_7)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_48.addWidget(self.label_21)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_35)


        self.verticalLayout_17.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.gridLayout_3 = QGridLayout(self.widget_8)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_24 = QLabel(self.widget_8)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 4, 0, 1, 1)

        self.label_22 = QLabel(self.widget_8)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 2, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.widget_8)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 35))
        self.lineEdit_9.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_3.addWidget(self.lineEdit_9, 1, 0, 1, 1)

        self.label_25 = QLabel(self.widget_8)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_3.addWidget(self.label_25, 6, 0, 1, 1)

        self.label_23 = QLabel(self.widget_8)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 0, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.widget_8)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 35))
        self.lineEdit_8.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_3.addWidget(self.lineEdit_8, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget_8)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 35))
        self.lineEdit_4.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_3.addWidget(self.lineEdit_4, 5, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.widget_8)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 35))
        self.lineEdit_10.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_3.addWidget(self.lineEdit_10, 7, 0, 1, 1)


        self.horizontalLayout_49.addWidget(self.widget_8)


        self.verticalLayout_17.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.save_client_btn = QPushButton(self.widget_7)
        self.save_client_btn.setObjectName(u"save_client_btn")
        self.save_client_btn.setMinimumSize(QSize(250, 35))
        self.save_client_btn.setMaximumSize(QSize(250, 35))
        self.save_client_btn.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;\n"
"font-size: 20px;\n"
"padding: 0;")

        self.horizontalLayout_50.addWidget(self.save_client_btn)


        self.verticalLayout_17.addLayout(self.horizontalLayout_50)


        self.horizontalLayout_47.addWidget(self.widget_7)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_36)


        self.verticalLayout_16.addLayout(self.horizontalLayout_47)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_17)


        self.horizontalLayout_11.addLayout(self.verticalLayout_16)

        self.page_supprimer_2.addTab(self.tab_formulaire_client, "")
        self.tab_formulaire_stocks = QWidget()
        self.tab_formulaire_stocks.setObjectName(u"tab_formulaire_stocks")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_formulaire_stocks)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_18)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalSpacer_37 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_37)

        self.widget_9 = QWidget(self.tab_formulaire_stocks)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(500, 0))
        self.widget_9.setMaximumSize(QSize(500, 16777215))
        self.widget_9.setStyleSheet(u"background: #fff;\n"
"color: #1c1c1c;")
        self.verticalLayout_19 = QVBoxLayout(self.widget_9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_38)

        self.label_28 = QLabel(self.widget_9)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_52.addWidget(self.label_28)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_39)


        self.verticalLayout_19.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_5 = QGridLayout(self.widget_10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_30 = QLabel(self.widget_10)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 0, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.widget_10)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(0, 35))
        self.lineEdit_13.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_5.addWidget(self.lineEdit_13, 5, 0, 1, 1)

        self.label_29 = QLabel(self.widget_10)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 2, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.widget_10)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(0, 35))
        self.lineEdit_15.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_5.addWidget(self.lineEdit_15, 1, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.widget_10)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(0, 35))
        self.lineEdit_14.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_5.addWidget(self.lineEdit_14, 3, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.widget_10)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 35))
        self.lineEdit_11.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_5.addWidget(self.lineEdit_11, 7, 0, 1, 1)

        self.label_31 = QLabel(self.widget_10)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_5.addWidget(self.label_31, 4, 0, 1, 1)

        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 6, 0, 1, 1)


        self.horizontalLayout_53.addWidget(self.widget_10)


        self.verticalLayout_19.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.save_produit_btn_3 = QPushButton(self.widget_9)
        self.save_produit_btn_3.setObjectName(u"save_produit_btn_3")
        self.save_produit_btn_3.setMinimumSize(QSize(300, 35))
        self.save_produit_btn_3.setMaximumSize(QSize(300, 35))
        self.save_produit_btn_3.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;\n"
"font-size: 20px;\n"
"padding: 0;")

        self.horizontalLayout_54.addWidget(self.save_produit_btn_3)


        self.verticalLayout_19.addLayout(self.horizontalLayout_54)


        self.horizontalLayout_51.addWidget(self.widget_9)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_40)


        self.verticalLayout_18.addLayout(self.horizontalLayout_51)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_19)


        self.horizontalLayout_12.addLayout(self.verticalLayout_18)

        self.page_supprimer_2.addTab(self.tab_formulaire_stocks, "")
        self.tab_formulaire_entrepots = QWidget()
        self.tab_formulaire_entrepots.setObjectName(u"tab_formulaire_entrepots")
        self.horizontalLayout_13 = QHBoxLayout(self.tab_formulaire_entrepots)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_20)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalSpacer_41 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_41)

        self.widget_11 = QWidget(self.tab_formulaire_entrepots)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(500, 0))
        self.widget_11.setMaximumSize(QSize(500, 16777215))
        self.widget_11.setStyleSheet(u"background: #fff;\n"
"color: #1c1c1c;")
        self.verticalLayout_21 = QVBoxLayout(self.widget_11)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_42)

        self.label_35 = QLabel(self.widget_11)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_56.addWidget(self.label_35)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_43)


        self.verticalLayout_21.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_7 = QGridLayout(self.widget_12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_20 = QLineEdit(self.widget_12)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(0, 35))
        self.lineEdit_20.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_7.addWidget(self.lineEdit_20, 3, 0, 1, 1)

        self.label_38 = QLabel(self.widget_12)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_7.addWidget(self.label_38, 4, 0, 1, 1)

        self.label_37 = QLabel(self.widget_12)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_7.addWidget(self.label_37, 0, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.widget_12)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(0, 35))
        self.lineEdit_21.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_7.addWidget(self.lineEdit_21, 1, 0, 1, 1)

        self.label_5 = QLabel(self.widget_12)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_36 = QLabel(self.widget_12)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_7.addWidget(self.label_36, 2, 0, 1, 1)

        self.lineEdit_19 = QLineEdit(self.widget_12)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(0, 35))
        self.lineEdit_19.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_7.addWidget(self.lineEdit_19, 5, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.widget_12)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(0, 35))
        self.lineEdit_12.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_7.addWidget(self.lineEdit_12, 7, 0, 1, 1)


        self.horizontalLayout_57.addWidget(self.widget_12)


        self.verticalLayout_21.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.save_produit_btn_4 = QPushButton(self.widget_11)
        self.save_produit_btn_4.setObjectName(u"save_produit_btn_4")
        self.save_produit_btn_4.setMinimumSize(QSize(250, 35))
        self.save_produit_btn_4.setMaximumSize(QSize(250, 35))
        self.save_produit_btn_4.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;\n"
"font-size: 20px;\n"
"padding: 0;")

        self.horizontalLayout_58.addWidget(self.save_produit_btn_4)


        self.verticalLayout_21.addLayout(self.horizontalLayout_58)


        self.horizontalLayout_55.addWidget(self.widget_11)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_44)


        self.verticalLayout_20.addLayout(self.horizontalLayout_55)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_21)


        self.horizontalLayout_13.addLayout(self.verticalLayout_20)

        self.page_supprimer_2.addTab(self.tab_formulaire_entrepots, "")
        self.tab_formulaire_entree = QWidget()
        self.tab_formulaire_entree.setObjectName(u"tab_formulaire_entree")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_formulaire_entree)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_22)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalSpacer_45 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_45)

        self.widget_22 = QWidget(self.tab_formulaire_entree)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMinimumSize(QSize(500, 0))
        self.widget_22.setMaximumSize(QSize(500, 16777215))
        self.widget_22.setStyleSheet(u"background: #fff;\n"
"color: #1c1c1c;")
        self.verticalLayout_23 = QVBoxLayout(self.widget_22)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_46)

        self.label_42 = QLabel(self.widget_22)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_60.addWidget(self.label_42)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_47)


        self.verticalLayout_23.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.widget_24 = QWidget(self.widget_22)
        self.widget_24.setObjectName(u"widget_24")
        self.gridLayout_9 = QGridLayout(self.widget_24)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lineEdit_26 = QLineEdit(self.widget_24)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMinimumSize(QSize(0, 35))
        self.lineEdit_26.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_9.addWidget(self.lineEdit_26, 3, 0, 1, 1)

        self.label_44 = QLabel(self.widget_24)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_9.addWidget(self.label_44, 0, 0, 1, 1)

        self.label_43 = QLabel(self.widget_24)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_9.addWidget(self.label_43, 2, 0, 1, 1)

        self.label_6 = QLabel(self.widget_24)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_9.addWidget(self.label_6, 7, 0, 1, 1)

        self.label_26 = QLabel(self.widget_24)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_9.addWidget(self.label_26, 9, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.widget_24)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(0, 35))
        self.lineEdit_16.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_9.addWidget(self.lineEdit_16, 8, 0, 1, 1)

        self.lineEdit_27 = QLineEdit(self.widget_24)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setMinimumSize(QSize(0, 35))
        self.lineEdit_27.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_9.addWidget(self.lineEdit_27, 1, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.widget_24)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(0, 35))
        self.lineEdit_17.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_9.addWidget(self.lineEdit_17, 10, 0, 1, 1)

        self.lineEdit_25 = QLineEdit(self.widget_24)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMinimumSize(QSize(0, 35))
        self.lineEdit_25.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_9.addWidget(self.lineEdit_25, 6, 0, 1, 1)

        self.label_45 = QLabel(self.widget_24)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_9.addWidget(self.label_45, 5, 0, 1, 1)


        self.horizontalLayout_61.addWidget(self.widget_24)


        self.verticalLayout_23.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.save_produit_btn_5 = QPushButton(self.widget_22)
        self.save_produit_btn_5.setObjectName(u"save_produit_btn_5")
        self.save_produit_btn_5.setMinimumSize(QSize(250, 35))
        self.save_produit_btn_5.setMaximumSize(QSize(250, 35))
        self.save_produit_btn_5.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;\n"
"font-size: 20px;\n"
"padding: 0;")

        self.horizontalLayout_62.addWidget(self.save_produit_btn_5)


        self.verticalLayout_23.addLayout(self.horizontalLayout_62)


        self.horizontalLayout_59.addWidget(self.widget_22)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_48)


        self.verticalLayout_22.addLayout(self.horizontalLayout_59)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_23)


        self.horizontalLayout_14.addLayout(self.verticalLayout_22)

        self.page_supprimer_2.addTab(self.tab_formulaire_entree, "")
        self.tab_formulaire_sorties = QWidget()
        self.tab_formulaire_sorties.setObjectName(u"tab_formulaire_sorties")
        self.horizontalLayout_15 = QHBoxLayout(self.tab_formulaire_sorties)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_24)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalSpacer_49 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_49)

        self.widget_27 = QWidget(self.tab_formulaire_sorties)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(500, 0))
        self.widget_27.setMaximumSize(QSize(500, 16777215))
        self.widget_27.setStyleSheet(u"background: #fff;\n"
"color: #1c1c1c;")
        self.verticalLayout_25 = QVBoxLayout(self.widget_27)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_50)

        self.label_49 = QLabel(self.widget_27)
        self.label_49.setObjectName(u"label_49")

        self.horizontalLayout_64.addWidget(self.label_49)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_51)


        self.verticalLayout_25.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.widget_28 = QWidget(self.widget_27)
        self.widget_28.setObjectName(u"widget_28")
        self.gridLayout_11 = QGridLayout(self.widget_28)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_50 = QLabel(self.widget_28)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_11.addWidget(self.label_50, 2, 0, 1, 1)

        self.label_32 = QLabel(self.widget_28)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_11.addWidget(self.label_32, 8, 0, 1, 1)

        self.label_52 = QLabel(self.widget_28)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_11.addWidget(self.label_52, 4, 0, 1, 1)

        self.label_27 = QLabel(self.widget_28)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_11.addWidget(self.label_27, 6, 0, 1, 1)

        self.lineEdit_32 = QLineEdit(self.widget_28)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setMinimumSize(QSize(0, 35))
        self.lineEdit_32.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_11.addWidget(self.lineEdit_32, 3, 0, 1, 1)

        self.lineEdit_33 = QLineEdit(self.widget_28)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setMinimumSize(QSize(0, 35))
        self.lineEdit_33.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_11.addWidget(self.lineEdit_33, 1, 0, 1, 1)

        self.lineEdit_31 = QLineEdit(self.widget_28)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setMinimumSize(QSize(0, 35))
        self.lineEdit_31.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_11.addWidget(self.lineEdit_31, 5, 0, 1, 1)

        self.lineEdit_18 = QLineEdit(self.widget_28)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(0, 35))
        self.lineEdit_18.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_11.addWidget(self.lineEdit_18, 7, 0, 1, 1)

        self.label_51 = QLabel(self.widget_28)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_11.addWidget(self.label_51, 0, 0, 1, 1)

        self.lineEdit_22 = QLineEdit(self.widget_28)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(0, 35))
        self.lineEdit_22.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_11.addWidget(self.lineEdit_22, 9, 0, 1, 1)


        self.horizontalLayout_65.addWidget(self.widget_28)


        self.verticalLayout_25.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.save_produit_btn_6 = QPushButton(self.widget_27)
        self.save_produit_btn_6.setObjectName(u"save_produit_btn_6")
        self.save_produit_btn_6.setMinimumSize(QSize(250, 35))
        self.save_produit_btn_6.setMaximumSize(QSize(250, 35))
        self.save_produit_btn_6.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;\n"
"font-size: 20px;\n"
"padding: 0;")

        self.horizontalLayout_66.addWidget(self.save_produit_btn_6)


        self.verticalLayout_25.addLayout(self.horizontalLayout_66)


        self.horizontalLayout_63.addWidget(self.widget_27)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_52)


        self.verticalLayout_24.addLayout(self.horizontalLayout_63)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_25)


        self.horizontalLayout_15.addLayout(self.verticalLayout_24)

        self.page_supprimer_2.addTab(self.tab_formulaire_sorties, "")
        self.tab_cf = QWidget()
        self.tab_cf.setObjectName(u"tab_cf")
        self.horizontalLayout_16 = QHBoxLayout(self.tab_cf)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_26)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalSpacer_53 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_53)

        self.widget_30 = QWidget(self.tab_cf)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMinimumSize(QSize(500, 0))
        self.widget_30.setMaximumSize(QSize(500, 16777215))
        self.widget_30.setStyleSheet(u"background: #fff;\n"
"color: #1c1c1c;")
        self.verticalLayout_27 = QVBoxLayout(self.widget_30)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_54)

        self.label_56 = QLabel(self.widget_30)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_68.addWidget(self.label_56)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_55)


        self.verticalLayout_27.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.widget_31 = QWidget(self.widget_30)
        self.widget_31.setObjectName(u"widget_31")
        self.gridLayout_13 = QGridLayout(self.widget_31)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lineEdit_37 = QLineEdit(self.widget_31)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setMinimumSize(QSize(0, 35))
        self.lineEdit_37.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_13.addWidget(self.lineEdit_37, 5, 0, 1, 1)

        self.lineEdit_38 = QLineEdit(self.widget_31)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setMinimumSize(QSize(0, 35))
        self.lineEdit_38.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_13.addWidget(self.lineEdit_38, 3, 0, 1, 1)

        self.label_57 = QLabel(self.widget_31)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_13.addWidget(self.label_57, 2, 0, 1, 1)

        self.lineEdit_39 = QLineEdit(self.widget_31)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setMinimumSize(QSize(0, 35))
        self.lineEdit_39.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_13.addWidget(self.lineEdit_39, 1, 0, 1, 1)

        self.label_58 = QLabel(self.widget_31)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_13.addWidget(self.label_58, 0, 0, 1, 1)

        self.label_59 = QLabel(self.widget_31)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_13.addWidget(self.label_59, 4, 0, 1, 1)


        self.horizontalLayout_69.addWidget(self.widget_31)


        self.verticalLayout_27.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.save_produit_btn_7 = QPushButton(self.widget_30)
        self.save_produit_btn_7.setObjectName(u"save_produit_btn_7")
        self.save_produit_btn_7.setMinimumSize(QSize(300, 35))
        self.save_produit_btn_7.setMaximumSize(QSize(300, 35))
        self.save_produit_btn_7.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;\n"
"font-size: 20px;\n"
"padding: 0;")

        self.horizontalLayout_70.addWidget(self.save_produit_btn_7)


        self.verticalLayout_27.addLayout(self.horizontalLayout_70)


        self.horizontalLayout_67.addWidget(self.widget_30)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_67.addItem(self.horizontalSpacer_56)


        self.verticalLayout_26.addLayout(self.horizontalLayout_67)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_27)


        self.horizontalLayout_16.addLayout(self.verticalLayout_26)

        self.page_supprimer_2.addTab(self.tab_cf, "")
        self.tab_formulaire_client1 = QWidget()
        self.tab_formulaire_client1.setObjectName(u"tab_formulaire_client1")
        self.horizontalLayout_17 = QHBoxLayout(self.tab_formulaire_client1)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_28)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalSpacer_57 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_57)

        self.widget_33 = QWidget(self.tab_formulaire_client1)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMinimumSize(QSize(500, 0))
        self.widget_33.setMaximumSize(QSize(500, 16777215))
        self.widget_33.setStyleSheet(u"background: #fff;\n"
"color: #1c1c1c;")
        self.verticalLayout_29 = QVBoxLayout(self.widget_33)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_58)

        self.label_63 = QLabel(self.widget_33)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_72.addWidget(self.label_63)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_59)


        self.verticalLayout_29.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.widget_34 = QWidget(self.widget_33)
        self.widget_34.setObjectName(u"widget_34")
        self.gridLayout_15 = QGridLayout(self.widget_34)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.lineEdit_43 = QLineEdit(self.widget_34)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setMinimumSize(QSize(0, 35))
        self.lineEdit_43.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_15.addWidget(self.lineEdit_43, 5, 0, 1, 1)

        self.lineEdit_44 = QLineEdit(self.widget_34)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setMinimumSize(QSize(0, 35))
        self.lineEdit_44.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_15.addWidget(self.lineEdit_44, 3, 0, 1, 1)

        self.label_64 = QLabel(self.widget_34)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_15.addWidget(self.label_64, 2, 0, 1, 1)

        self.lineEdit_45 = QLineEdit(self.widget_34)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setMinimumSize(QSize(0, 35))
        self.lineEdit_45.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_15.addWidget(self.lineEdit_45, 1, 0, 1, 1)

        self.label_65 = QLabel(self.widget_34)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_15.addWidget(self.label_65, 0, 0, 1, 1)

        self.label_66 = QLabel(self.widget_34)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_15.addWidget(self.label_66, 4, 0, 1, 1)


        self.horizontalLayout_73.addWidget(self.widget_34)


        self.verticalLayout_29.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.save_produit_btn_8 = QPushButton(self.widget_33)
        self.save_produit_btn_8.setObjectName(u"save_produit_btn_8")
        self.save_produit_btn_8.setMinimumSize(QSize(320, 35))
        self.save_produit_btn_8.setMaximumSize(QSize(320, 35))
        self.save_produit_btn_8.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;\n"
"font-size: 20px;\n"
"padding: 0;")

        self.horizontalLayout_74.addWidget(self.save_produit_btn_8)


        self.verticalLayout_29.addLayout(self.horizontalLayout_74)


        self.horizontalLayout_71.addWidget(self.widget_33)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_60)


        self.verticalLayout_28.addLayout(self.horizontalLayout_71)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_29)


        self.horizontalLayout_17.addLayout(self.verticalLayout_28)

        self.page_supprimer_2.addTab(self.tab_formulaire_client1, "")
        self.tab_formulaire_utilisateur = QWidget()
        self.tab_formulaire_utilisateur.setObjectName(u"tab_formulaire_utilisateur")
        self.horizontalLayout_18 = QHBoxLayout(self.tab_formulaire_utilisateur)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_30)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalSpacer_61 = QSpacerItem(78, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_61)

        self.widget_36 = QWidget(self.tab_formulaire_utilisateur)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setMinimumSize(QSize(500, 0))
        self.widget_36.setMaximumSize(QSize(500, 16777215))
        self.widget_36.setStyleSheet(u"background: #fff;\n"
"color: #1c1c1c;")
        self.verticalLayout_31 = QVBoxLayout(self.widget_36)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_62)

        self.label_70 = QLabel(self.widget_36)
        self.label_70.setObjectName(u"label_70")

        self.horizontalLayout_76.addWidget(self.label_70)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_63)


        self.verticalLayout_31.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.widget_37 = QWidget(self.widget_36)
        self.widget_37.setObjectName(u"widget_37")
        self.gridLayout_17 = QGridLayout(self.widget_37)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_72 = QLabel(self.widget_37)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_17.addWidget(self.label_72, 0, 0, 1, 1)

        self.lineEdit_50 = QLineEdit(self.widget_37)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setMinimumSize(QSize(0, 35))
        self.lineEdit_50.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_17.addWidget(self.lineEdit_50, 3, 0, 1, 1)

        self.label_71 = QLabel(self.widget_37)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_17.addWidget(self.label_71, 2, 0, 1, 1)

        self.lineEdit_51 = QLineEdit(self.widget_37)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setMinimumSize(QSize(0, 35))
        self.lineEdit_51.setMaximumSize(QSize(16777215, 35))

        self.gridLayout_17.addWidget(self.lineEdit_51, 1, 0, 1, 1)


        self.horizontalLayout_77.addWidget(self.widget_37)


        self.verticalLayout_31.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.save_produit_btn_9 = QPushButton(self.widget_36)
        self.save_produit_btn_9.setObjectName(u"save_produit_btn_9")
        self.save_produit_btn_9.setMinimumSize(QSize(250, 35))
        self.save_produit_btn_9.setMaximumSize(QSize(250, 35))
        self.save_produit_btn_9.setStyleSheet(u"background: #4b7bb2;\n"
"color: #fff;\n"
"font-size: 20px;\n"
"padding: 0;")

        self.horizontalLayout_78.addWidget(self.save_produit_btn_9)


        self.verticalLayout_31.addLayout(self.horizontalLayout_78)


        self.horizontalLayout_75.addWidget(self.widget_36)

        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_64)


        self.verticalLayout_30.addLayout(self.horizontalLayout_75)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_31)


        self.horizontalLayout_18.addLayout(self.verticalLayout_30)

        self.page_supprimer_2.addTab(self.tab_formulaire_utilisateur, "")

        self.horizontalLayout_41.addWidget(self.page_supprimer_2)

        self.MainTable.addTab(self.OptionTab, "")

        self.horizontalLayout_2.addWidget(self.MainTable)


        self.horizontalLayout.addWidget(self.mainPage)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.MainTable.setCurrentIndex(10)
        self.page_supprimer_2.setCurrentIndex(10)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.table_produit.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"nom_produit", None));
        ___qtablewidgetitem1 = self.table_produit.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"description", None));
        ___qtablewidgetitem2 = self.table_produit.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"code_barres", None));
        ___qtablewidgetitem3 = self.table_produit.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"id_categorie", None));
        ___qtablewidgetitem4 = self.table_produit.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"prix_achat", None));
        ___qtablewidgetitem5 = self.table_produit.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"prix_vente", None));
        ___qtablewidgetitem6 = self.table_produit.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"seuil_alerte", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.supprimer_produit_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actualiser_produit_btn.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.produit_page), QCoreApplication.translate("MainWindow", u"Produits", None))
        ___qtablewidgetitem7 = self.table_client.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"nom_client", None));
        ___qtablewidgetitem8 = self.table_client.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"adresse", None));
        ___qtablewidgetitem9 = self.table_client.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"telephone", None));
        ___qtablewidgetitem10 = self.table_client.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"email", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.supprimer_client_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actualiser_client_btn.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.page_client), QCoreApplication.translate("MainWindow", u"Clients", None))
        ___qtablewidgetitem11 = self.table_stocks.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"id_produit", None));
        ___qtablewidgetitem12 = self.table_stocks.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"id_entrepot", None));
        ___qtablewidgetitem13 = self.table_stocks.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"quantite", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.supprimer_stocks_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actualiser_stocks_btn.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.page_stocks), QCoreApplication.translate("MainWindow", u"Stocks", None))
        ___qtablewidgetitem14 = self.table_fournisseur.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"nom_fournisseur", None));
        ___qtablewidgetitem15 = self.table_fournisseur.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"adresse", None));
        ___qtablewidgetitem16 = self.table_fournisseur.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"telephone", None));
        ___qtablewidgetitem17 = self.table_fournisseur.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"email", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.supprimer_fournisseur_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actualiser_fournisseur_btn.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.page_fournisseur), QCoreApplication.translate("MainWindow", u"Fournisseurs", None))
        ___qtablewidgetitem18 = self.table_entrepot.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"nom_entrepot", None));
        ___qtablewidgetitem19 = self.table_entrepot.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"adresse", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.supprimer_entrepots_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actualiser_entrepots_btn.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.page_entrepot), QCoreApplication.translate("MainWindow", u"Entrepots", None))
        ___qtablewidgetitem20 = self.table_entrees.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"id_fournisseur", None));
        ___qtablewidgetitem21 = self.table_entrees.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"date_entree", None));
        ___qtablewidgetitem22 = self.table_entrees.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"id_produit", None));
        ___qtablewidgetitem23 = self.table_entrees.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"quantite", None));
        ___qtablewidgetitem24 = self.table_entrees.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"id_entrepot", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.supprimer_entrees_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actualiser_entrees_btn.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.page_entrees), QCoreApplication.translate("MainWindow", u"Entrees", None))
        ___qtablewidgetitem25 = self.table_sorties.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"id_client", None));
        ___qtablewidgetitem26 = self.table_sorties.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"date_sorties", None));
        ___qtablewidgetitem27 = self.table_sorties.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"id_produit", None));
        ___qtablewidgetitem28 = self.table_sorties.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"quantite", None));
        ___qtablewidgetitem29 = self.table_sorties.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"id_entrepot", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.supprimer_sorties_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actualiser_sorties_btn.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.page_sorties), QCoreApplication.translate("MainWindow", u"Sorties", None))
        ___qtablewidgetitem30 = self.table_commande_f.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"id_fournisseur", None));
        ___qtablewidgetitem31 = self.table_commande_f.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"date_commande", None));
        ___qtablewidgetitem32 = self.table_commande_f.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"statut", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.supprimer_cf_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actualiser_cf_btn.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.page_c_fournisseur), QCoreApplication.translate("MainWindow", u"Commande Fournissaur", None))
        ___qtablewidgetitem33 = self.table_commande_c.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"id_client", None));
        ___qtablewidgetitem34 = self.table_commande_c.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"date_commande", None));
        ___qtablewidgetitem35 = self.table_commande_c.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"statut", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.supprimer_cc_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actualiser_cc_btn.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Commande Clients", None))
        ___qtablewidgetitem36 = self.table_produit_11.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"nom_utilisateur", None));
        ___qtablewidgetitem37 = self.table_produit_11.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"mot_de_passe", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.supprimer_utilisateur_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.actualiser_utilisateur_btn.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.page_utilisateur), QCoreApplication.translate("MainWindow", u"Utilisateurs", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Formulaire de produits", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Descriptions", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Nom Produit", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Code Barres", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Prix Achat", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Prix Vente", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Seuil Alerte", None))
        self.save_produit_btn.setText(QCoreApplication.translate("MainWindow", u"Enregistrer les produit", None))
        self.page_supprimer_2.setTabText(self.page_supprimer_2.indexOf(self.tab_formulaire_produits), QCoreApplication.translate("MainWindow", u"Formulaire_Produits", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Formulaire de client", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Telephone", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Nom Client", None))
        self.save_client_btn.setText(QCoreApplication.translate("MainWindow", u"Enregistrer le client", None))
        self.page_supprimer_2.setTabText(self.page_supprimer_2.indexOf(self.tab_formulaire_client), QCoreApplication.translate("MainWindow", u"Formulaire Client", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Formulaire de fournisseur", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Nom fournisseur", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Telephone", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.save_produit_btn_3.setText(QCoreApplication.translate("MainWindow", u"Enregistrer le fournisseur", None))
        self.page_supprimer_2.setTabText(self.page_supprimer_2.indexOf(self.tab_formulaire_stocks), QCoreApplication.translate("MainWindow", u"Formulaire Stocks", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Formulaire de entrepot", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Telephone", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Nom fournisseur", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.save_produit_btn_4.setText(QCoreApplication.translate("MainWindow", u"Enregistrer l'entrepot", None))
        self.page_supprimer_2.setTabText(self.page_supprimer_2.indexOf(self.tab_formulaire_entrepots), QCoreApplication.translate("MainWindow", u"Formulaire Entrepots", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Formulaire de entrees", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Id fournisseur", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Date entree", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Quantite", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Id entrepot", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Id produit", None))
        self.save_produit_btn_5.setText(QCoreApplication.translate("MainWindow", u"Enregistrer l'entree", None))
        self.page_supprimer_2.setTabText(self.page_supprimer_2.indexOf(self.tab_formulaire_entree), QCoreApplication.translate("MainWindow", u"Formulaire Entrees", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Formulaire de sorties", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Date sortie", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Id entrepot", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Id produit", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Quantite", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Id client", None))
        self.save_produit_btn_6.setText(QCoreApplication.translate("MainWindow", u"Enregistrer les sorties", None))
        self.page_supprimer_2.setTabText(self.page_supprimer_2.indexOf(self.tab_formulaire_sorties), QCoreApplication.translate("MainWindow", u"Formulaire Sorties", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Commande Fournisseur", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Date commande", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Id fournisseur", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Statut", None))
        self.save_produit_btn_7.setText(QCoreApplication.translate("MainWindow", u"Enregistrer commande cf", None))
        self.page_supprimer_2.setTabText(self.page_supprimer_2.indexOf(self.tab_cf), QCoreApplication.translate("MainWindow", u"Commande Fournisseur", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Formulaire de commande client", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Date commande", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Id fournisseur", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Statut", None))
        self.save_produit_btn_8.setText(QCoreApplication.translate("MainWindow", u"Enregistrer le commande client", None))
        self.page_supprimer_2.setTabText(self.page_supprimer_2.indexOf(self.tab_formulaire_client1), QCoreApplication.translate("MainWindow", u"Commande Client", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Formulaire d'utilisateur", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Nom utilisateur", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.save_produit_btn_9.setText(QCoreApplication.translate("MainWindow", u"Enregistrer l'utilisateur", None))
        self.page_supprimer_2.setTabText(self.page_supprimer_2.indexOf(self.tab_formulaire_utilisateur), QCoreApplication.translate("MainWindow", u"Formulaire Utilisateur", None))
        self.MainTable.setTabText(self.MainTable.indexOf(self.OptionTab), QCoreApplication.translate("MainWindow", u"page_option", None))
    # retranslateUi

