# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDial, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(776, 851)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 40, 931, 751))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 20, 681, 321))
        self.gridLayoutWidget_4 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 70, 294, 241))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 7, 3, 1, 1)

        self.btn_SV_Dispense = QPushButton(self.gridLayoutWidget_4)
        self.btn_SV_Dispense.setObjectName(u"btn_SV_Dispense")

        self.gridLayout_4.addWidget(self.btn_SV_Dispense, 8, 3, 1, 1)

        self.btn_SP_Disp = QPushButton(self.gridLayoutWidget_4)
        self.btn_SP_Disp.setObjectName(u"btn_SP_Disp")

        self.gridLayout_4.addWidget(self.btn_SP_Disp, 4, 3, 1, 1)

        self.lb_SP_CurPos = QLabel(self.gridLayoutWidget_4)
        self.lb_SP_CurPos.setObjectName(u"lb_SP_CurPos")
        self.lb_SP_CurPos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.lb_SP_CurPos, 1, 3, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_4)
        self.label_25.setObjectName(u"label_25")
        font = QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)

        self.gridLayout_4.addWidget(self.label_25, 3, 4, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_4)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_27, 5, 2, 1, 1)

        self.btn_SP_Move = QPushButton(self.gridLayoutWidget_4)
        self.btn_SP_Move.setObjectName(u"btn_SP_Move")

        self.gridLayout_4.addWidget(self.btn_SP_Move, 6, 3, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.gridLayout_4.addWidget(self.label_29, 1, 4, 1, 1)

        self.btn_SP_Home = QPushButton(self.gridLayoutWidget_4)
        self.btn_SP_Home.setObjectName(u"btn_SP_Home")

        self.gridLayout_4.addWidget(self.btn_SP_Home, 1, 0, 1, 2)

        self.le_SP_TargetPos = QLineEdit(self.gridLayoutWidget_4)
        self.le_SP_TargetPos.setObjectName(u"le_SP_TargetPos")
        self.le_SP_TargetPos.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.le_SP_TargetPos, 5, 3, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_4)
        self.label_22.setObjectName(u"label_22")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_22, 0, 0, 1, 2)

        self.btn_SP_Aspi = QPushButton(self.gridLayoutWidget_4)
        self.btn_SP_Aspi.setObjectName(u"btn_SP_Aspi")

        self.gridLayout_4.addWidget(self.btn_SP_Aspi, 2, 3, 1, 1)

        self.le_SP_Volume = QLineEdit(self.gridLayoutWidget_4)
        self.le_SP_Volume.setObjectName(u"le_SP_Volume")
        self.le_SP_Volume.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.le_SP_Volume, 3, 3, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_23, 3, 2, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_4.addWidget(self.label_24, 5, 4, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_26, 1, 2, 1, 1)

        self.gridLayoutWidget_5 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(320, 70, 393, 221))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.gridLayoutWidget_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout_5.addWidget(self.label_37, 1, 2, 1, 1)

        self.lb_SP_TopState = QLabel(self.gridLayoutWidget_5)
        self.lb_SP_TopState.setObjectName(u"lb_SP_TopState")
        self.lb_SP_TopState.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.lb_SP_TopState, 2, 4, 1, 1)

        self.lb_SP_LeftState = QLabel(self.gridLayoutWidget_5)
        self.lb_SP_LeftState.setObjectName(u"lb_SP_LeftState")
        self.lb_SP_LeftState.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout_5.addWidget(self.lb_SP_LeftState, 2, 2, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_5.addWidget(self.label_35, 1, 4, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout_5.addWidget(self.label_31, 6, 3, 1, 1)

        self.label_38 = QLabel(self.gridLayoutWidget_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_38, 0, 2, 1, 1)

        self.lb_SP_BottomState = QLabel(self.gridLayoutWidget_5)
        self.lb_SP_BottomState.setObjectName(u"lb_SP_BottomState")
        self.lb_SP_BottomState.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_5.addWidget(self.lb_SP_BottomState, 7, 3, 1, 1)

        self.dial_Dir = QDial(self.gridLayoutWidget_5)
        self.dial_Dir.setObjectName(u"dial_Dir")
        self.dial_Dir.setMinimum(1)
        self.dial_Dir.setMaximum(3)
        self.dial_Dir.setSingleStep(1)
        self.dial_Dir.setPageStep(10)
        self.dial_Dir.setValue(1)
        self.dial_Dir.setSliderPosition(1)
        self.dial_Dir.setOrientation(Qt.Horizontal)
        self.dial_Dir.setInvertedAppearance(False)
        self.dial_Dir.setInvertedControls(False)
        self.dial_Dir.setWrapping(False)
        self.dial_Dir.setNotchTarget(3.700000000000000)
        self.dial_Dir.setNotchesVisible(False)

        self.gridLayout_5.addWidget(self.dial_Dir, 4, 3, 2, 1)

        self.gridLayoutWidget_6 = QWidget(self.groupBox_3)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 20, 230, 51))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.gridLayoutWidget_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_39, 1, 0, 1, 1)

        self.lb_SP_State = QLabel(self.gridLayoutWidget_6)
        self.lb_SP_State.setObjectName(u"lb_SP_State")

        self.gridLayout_6.addWidget(self.lb_SP_State, 0, 1, 1, 1)

        self.cb_SP_Comport = QComboBox(self.gridLayoutWidget_6)
        self.cb_SP_Comport.setObjectName(u"cb_SP_Comport")

        self.gridLayout_6.addWidget(self.cb_SP_Comport, 1, 1, 1, 1)

        self.label_41 = QLabel(self.gridLayoutWidget_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_41, 0, 0, 1, 1)

        self.btn_SP_Connect = QPushButton(self.gridLayoutWidget_6)
        self.btn_SP_Connect.setObjectName(u"btn_SP_Connect")

        self.gridLayout_6.addWidget(self.btn_SP_Connect, 1, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 340, 481, 351))
        self.table_Ardu_IO = QTableWidget(self.groupBox_4)
        if (self.table_Ardu_IO.columnCount() < 4):
            self.table_Ardu_IO.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_Ardu_IO.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_Ardu_IO.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_Ardu_IO.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_Ardu_IO.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.table_Ardu_IO.rowCount() < 6):
            self.table_Ardu_IO.setRowCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_Ardu_IO.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_Ardu_IO.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_Ardu_IO.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_Ardu_IO.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_Ardu_IO.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_Ardu_IO.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(0, 3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(1, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(1, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(1, 3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(2, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(2, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(2, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(2, 3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(3, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(3, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(3, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(3, 3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(4, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(4, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(4, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(4, 3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(5, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_Ardu_IO.setItem(5, 1, __qtablewidgetitem31)
        self.table_Ardu_IO.setObjectName(u"table_Ardu_IO")
        self.table_Ardu_IO.setGeometry(QRect(0, 110, 481, 231))
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 90, 56, 12))
        self.gridLayoutWidget_7 = QWidget(self.groupBox_4)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 20, 230, 51))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.gridLayoutWidget_7)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_42, 1, 0, 1, 1)

        self.lb_Ardu_State = QLabel(self.gridLayoutWidget_7)
        self.lb_Ardu_State.setObjectName(u"lb_Ardu_State")

        self.gridLayout_7.addWidget(self.lb_Ardu_State, 0, 1, 1, 1)

        self.cb_Ardu_Comport = QComboBox(self.gridLayoutWidget_7)
        self.cb_Ardu_Comport.setObjectName(u"cb_Ardu_Comport")

        self.gridLayout_7.addWidget(self.cb_Ardu_Comport, 1, 1, 1, 1)

        self.label_44 = QLabel(self.gridLayoutWidget_7)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.label_44, 0, 0, 1, 1)

        self.btn_Ardu_Connect = QPushButton(self.gridLayoutWidget_7)
        self.btn_Ardu_Connect.setObjectName(u"btn_Ardu_Connect")

        self.gridLayout_7.addWidget(self.btn_Ardu_Connect, 1, 2, 1, 1)

        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(500, 340, 221, 111))
        self.gridLayoutWidget = QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 20, 181, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.le_SV_24VKeepTime = QLineEdit(self.gridLayoutWidget)
        self.le_SV_24VKeepTime.setObjectName(u"le_SV_24VKeepTime")
        self.le_SV_24VKeepTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_SV_24VKeepTime, 1, 1, 1, 1)

        self.le_SV_8VKeepTime = QLineEdit(self.gridLayoutWidget)
        self.le_SV_8VKeepTime.setObjectName(u"le_SV_8VKeepTime")
        self.le_SV_8VKeepTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_SV_8VKeepTime, 2, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.le_SV_MaxTime = QLineEdit(self.gridLayoutWidget)
        self.le_SV_MaxTime.setObjectName(u"le_SV_MaxTime")
        self.le_SV_MaxTime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.le_SV_MaxTime, 3, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(500, 470, 221, 111))
        self.gridLayoutWidget_2 = QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 20, 171, 80))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.le_S_PulseperUnit = QLineEdit(self.gridLayoutWidget_2)
        self.le_S_PulseperUnit.setObjectName(u"le_S_PulseperUnit")
        self.le_S_PulseperUnit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.le_S_PulseperUnit, 0, 1, 1, 1)

        self.le_S_AspiSpeed = QLineEdit(self.gridLayoutWidget_2)
        self.le_S_AspiSpeed.setObjectName(u"le_S_AspiSpeed")
        self.le_S_AspiSpeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.le_S_AspiSpeed, 1, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.le_S_DispSpeed = QLineEdit(self.gridLayoutWidget_2)
        self.le_S_DispSpeed.setObjectName(u"le_S_DispSpeed")
        self.le_S_DispSpeed.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.le_S_DispSpeed, 2, 1, 1, 1)

        self.btn_Save = QPushButton(self.tab_2)
        self.btn_Save.setObjectName(u"btn_Save")
        self.btn_Save.setGeometry(QRect(520, 640, 75, 23))
        self.btn_Load = QPushButton(self.tab_2)
        self.btn_Load.setObjectName(u"btn_Load")
        self.btn_Load.setGeometry(QRect(620, 640, 75, 23))
        self.gridLayoutWidget_3 = QWidget(self.tab_2)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(530, 580, 171, 46))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.le_Ardu_IONum = QLineEdit(self.gridLayoutWidget_3)
        self.le_Ardu_IONum.setObjectName(u"le_Ardu_IONum")
        self.le_Ardu_IONum.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.le_Ardu_IONum, 0, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.groupBox_3.setTitle("")
        self.btn_SV_Dispense.setText(QCoreApplication.translate("MainWindow", u"\uc194\ubca8\ube0c \ubd84\uc8fc", None))
        self.btn_SP_Disp.setText(QCoreApplication.translate("MainWindow", u"\ubd84\uc8fc", None))
        self.lb_SP_CurPos.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"ul", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\ubaa9\ud45c \uac12", None))
        self.btn_SP_Move.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub3d9", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"ul", None))
        self.btn_SP_Home.setText(QCoreApplication.translate("MainWindow", u"\ucd08\uae30\ud654", None))
        self.le_SP_TargetPos.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\ub9b0\uc9c0", None))
        self.btn_SP_Aspi.setText(QCoreApplication.translate("MainWindow", u"\ud761\uc785", None))
        self.le_SP_Volume.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\ud761\uc785/\ubd84\uc8fc \ub7c9", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"ul", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac  \uac12", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc774\ud3ab", None))
        self.lb_SP_TopState.setText(QCoreApplication.translate("MainWindow", u"NeedHome", None))
        self.lb_SP_LeftState.setText(QCoreApplication.translate("MainWindow", u"NeedHome", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\uc555\ub825\uc6a9\uae30", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\ub9b0\uc9c0", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\ub9b0\uc9c0 \ubc29\ud5a5", None))
        self.lb_SP_BottomState.setText(QCoreApplication.translate("MainWindow", u"NeedHome", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Comport", None))
        self.lb_SP_State.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\uc5f0\uacb0 \uc0c1\ud0dc", None))
        self.btn_SP_Connect.setText(QCoreApplication.translate("MainWindow", u"\uc5f0\uacb0", None))
        self.groupBox_4.setTitle("")
        ___qtablewidgetitem = self.table_Ardu_IO.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem1 = self.table_Ardu_IO.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Num", None));
        ___qtablewidgetitem2 = self.table_Ardu_IO.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.table_Ardu_IO.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None));
        ___qtablewidgetitem4 = self.table_Ardu_IO.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem5 = self.table_Ardu_IO.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem6 = self.table_Ardu_IO.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem7 = self.table_Ardu_IO.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem8 = self.table_Ardu_IO.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"-", None));
        ___qtablewidgetitem9 = self.table_Ardu_IO.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"-", None));

        __sortingEnabled = self.table_Ardu_IO.isSortingEnabled()
        self.table_Ardu_IO.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.table_Ardu_IO.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Disable", None));
        ___qtablewidgetitem11 = self.table_Ardu_IO.item(0, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem12 = self.table_Ardu_IO.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Input", None));
        ___qtablewidgetitem13 = self.table_Ardu_IO.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem14 = self.table_Ardu_IO.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\uc555\ub825\uc13c\uc11c", None));
        ___qtablewidgetitem15 = self.table_Ardu_IO.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Off", None));
        ___qtablewidgetitem16 = self.table_Ardu_IO.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Output", None));
        ___qtablewidgetitem17 = self.table_Ardu_IO.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem18 = self.table_Ardu_IO.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\uacf5\uc555\ud38c\ud504", None));
        ___qtablewidgetitem19 = self.table_Ardu_IO.item(2, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Off", None));
        ___qtablewidgetitem20 = self.table_Ardu_IO.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Output", None));
        ___qtablewidgetitem21 = self.table_Ardu_IO.item(3, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem22 = self.table_Ardu_IO.item(3, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\uc194\ubca8\ube0c", None));
        ___qtablewidgetitem23 = self.table_Ardu_IO.item(3, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Off", None));
        ___qtablewidgetitem24 = self.table_Ardu_IO.item(4, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Output", None));
        ___qtablewidgetitem25 = self.table_Ardu_IO.item(4, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem26 = self.table_Ardu_IO.item(4, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\ud301\ub9ac\uc81d", None));
        ___qtablewidgetitem27 = self.table_Ardu_IO.item(4, 3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Off", None));
        ___qtablewidgetitem28 = self.table_Ardu_IO.item(5, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Disable", None));
        ___qtablewidgetitem29 = self.table_Ardu_IO.item(5, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"6", None));
        self.table_Ardu_IO.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"- I/O -", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Comport", None))
        self.lb_Ardu_State.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\uc5f0\uacb0 \uc0c1\ud0dc", None))
        self.btn_Ardu_Connect.setText(QCoreApplication.translate("MainWindow", u"\uc5f0\uacb0", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"24V \uc720\uc9c0 \uc2dc\uac04", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"8V \uc720\uc9c0 \uc2dc\uac04", None))
        self.le_SV_24VKeepTime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.le_SV_8VKeepTime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Max \uc2dc\uac04", None))
        self.le_SV_MaxTime.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.groupBox_2.setTitle("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Pulse per Unit", None))
        self.le_S_PulseperUnit.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.le_S_AspiSpeed.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\ud761\uc785 \uc18d\ub3c4(ul/s)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\ubd84\uc8fc \uc18d\ub3c4(ul/s)", None))
        self.le_S_DispSpeed.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_Load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.le_Ardu_IONum.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Arduino IO \uac2f\uc218", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"maintenance", None))
    # retranslateUi

