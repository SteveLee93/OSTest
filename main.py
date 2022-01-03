import sys
import threading
import time

import serial.tools.list_ports

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIntValidator, QCloseEvent

from ui import Ui_MainWindow
from syringeModule import Syringe
from arduino import Arduino
from qt_material import apply_stylesheet

SP = Syringe()
Ardu = Arduino()

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.MainUIConnect()

        self.LoadConnectedPort()
        
        self.SetThread()

        self.SaveSetting()

    def closeEvent(self, QCloseEvent):
        if Ardu.IsConnected() == True:
            Ardu.Close()
        if SP.IsConnected() == True:
            SP.Close()

        
    def MainUIConnect(self):
        self.ui.btn_SP_Connect.clicked.connect(self.SP_Connect)
        self.ui.btn_SP_Home.clicked.connect(self.SP_Home)
        self.ui.dial_Dir.valueChanged.connect(self.SP_ChangeDir)
        self.SetLineEditRange()
        self.ui.btn_SP_Aspi.clicked.connect(self.SP_Aspirate)
        self.ui.btn_SP_Disp.clicked.connect(self.SP_Dispense)
        self.ui.btn_SP_Move.clicked.connect(self.SP_Move)
        self.ui.btn_Save.clicked.connect(self.SaveSetting)
        self.ui.btn_Load.clicked.connect(self.LoadSetting)
        self.ui.btn_Ardu_Connect.clicked.connect(self.Ardu_Connect)
        self.ui.table_Ardu_IO.cellClicked.connect(self.Ardu_IOClicked)
        self.ui.btn_SV_Dispense.clicked.connect(self.SP_SolValveDispense)

    def Ardu_Connect(self):
        comport = self.ui.cb_Ardu_Comport.currentText()
        Ardu.Connect(comport)
        time.sleep(1)
        if Ardu.IsConnected() == True:
            self.thread_Ardu_Monitoring.start()

    def Ardu_SetIOTable(self):
        io_count = int(self.ui.le_Ardu_IONum.text())

        for num in range(0, io_count):
            io_state = Ardu.GetIOState(num)
            # io_state = 'Off'
            self.ui.table_Ardu_IO.item(num,3).setText(io_state)
    
    def Ardu_IOClicked(self, r, c):

        io_type = self.ui.table_Ardu_IO.item(r,0).text()
        io_number = self.ui.table_Ardu_IO.item(r,1).text()
        io_name = self.ui.table_Ardu_IO.item(r,2).text()
        io_state = self.ui.table_Ardu_IO.item(r,3).text()

        if io_type == "Input":
            pass
        elif io_type == "Output":
            if io_state == "Off":
                Ardu.SetOutput(io_number, True)
                self.ui.table_Ardu_IO.item(r,3).setText('On')
            elif io_state == "On":
                Ardu.SetOutput(io_number, False)
                self.ui.table_Ardu_IO.item(r,3).setText('Off')

        # print(f"io_type = {io_type}")
        # print(f"io_number = {io_number}")
        # print(f"io_name = {io_name}")
        # print(f"io_state = {io_state}")
    
    def Ardu_Monitoring(self):
        while True:
            try:
                time.sleep(0.5)
                if Ardu.IsConnected() == False:
                    self.ui.lb_Ardu_State.setText("Disconnect")
                else:
                    self.ui.lb_Ardu_State.setText("Connect")
                for io in range(2,7):
                    result = Ardu.GetIOState(io).replace('\r\n','')
                    if io == 2: # 압력센서 처리
                        if result == '0': # 센서 On
                            pumpstate = Ardu.GetIOState(3).replace('\r\n','')
                            if pumpstate == '0':
                                Ardu.SetOutput(3, False) # 펌프 Off
                                time.sleep(0.5)

                        elif result == '1': # 센서 Off
                            pumpstate = Ardu.GetIOState(3).replace('\r\n','')
                            if pumpstate == '1':
                                Ardu.SetOutput(3, True) # 펌프 On
                                time.sleep(0.5)

                    if result == '0': result = 'On'
                    elif result == '1': result = 'Off'
                    self.ui.table_Ardu_IO.item(io-1,3).setText(result)
                    # print(f"io.{io} = {result}")
            except:
                pass

    def SaveSetting(self):
        maxtime_sol = self.ui.le_SV_MaxTime.text()
        Ardu.SetMaxTime(maxtime_sol)
        pulseperunit = int(self.ui.le_S_PulseperUnit.text())
        self.SP_SetPulsePerUnit(pulseperunit)
        pass

    def LoadSetting(self):
        pass
        
    def SetThread(self):
        self.thread_SP_Monitoring = threading.Thread(target = self.SP_Monitoring)
        self.thread_SP_Monitoring.daemon = True
        self.thread_Ardu_Monitoring = threading.Thread(target = self.Ardu_Monitoring)
        self.thread_Ardu_Monitoring.daemon = True

    def SetLineEditRange(self):
        self.ui.le_Ardu_IONum.setValidator(QIntValidator(1,9))
        self.ui.le_SP_Volume.setValidator(QIntValidator(1,9999))
        self.ui.le_SP_TargetPos.setValidator(QIntValidator(1,9999))
        self.ui.le_SV_24VKeepTime.setValidator(QIntValidator(1,9999))
        self.ui.le_SV_8VKeepTime.setValidator(QIntValidator(1,9999))
        self.ui.le_SV_MaxTime.setValidator(QIntValidator(1,9999000))
        self.ui.le_S_AspiSpeed.setValidator(QIntValidator(1,9999))
        self.ui.le_S_DispSpeed.setValidator(QIntValidator(1,9999))
        self.ui.le_S_PulseperUnit.setValidator(QIntValidator(1,9999))

    def LoadConnectedPort(self):
        ports = serial.tools.list_ports.comports()
        portlist =[]
        for port in ports:
            portlist.append(port[0])

        for port in portlist:
            self.ui.cb_SP_Comport.addItem(port)
            self.ui.cb_Ardu_Comport.addItem(port)

    def SP_Monitoring(self):
        while True:
            try:
                time.sleep(1)
                if SP.IsConnected() == False:
                    self.ui.lb_SP_State.setText("Disconnect")
                else:
                    self.ui.lb_SP_State.setText("Connect")
                currentpos = SP.GetCurPosition()
                self.ui.lb_SP_CurPos.setText(str(currentpos))
            except:
                pass

    def SP_Aspirate(self):
        # 시린지 방향 I로 변경
        if SP.ChangeValveDir(1) == True:
            self.SP_UIChangeDirState(1)
        time.sleep(0.5)

        # 솔벨브 Time 조정.
        Ardu.SetMaxTime('2000')
        time.sleep(0.5)

        # 솔벨브 On > 자동 Off 됨.
        Ardu.SetOutput(4, True)

        # 시린지 흡입
        ul = int(self.ui.le_SP_Volume.text())
        SP.ReMoveSyringe(ul)
        
    def SP_Dispense(self):
        # 시린지 방향 I로 변경
        if SP.ChangeValveDir(1) == True:
            self.SP_UIChangeDirState(1)
        time.sleep(0.5)

        # 솔벨브 Time 조정.
        Ardu.SetMaxTime('2000')
        time.sleep(0.5)

        # 솔벨브 On > 자동 Off 됨.
        Ardu.SetOutput(4, True)

        # 시린지 분주
        ul = int(self.ui.le_SP_Volume.text()) * -1
        SP.ReMoveSyringe(ul)

    def SP_Move(self):
        # 시린지 방향 I로 변경
        if SP.ChangeValveDir(1) == True:
            self.SP_UIChangeDirState(1)
        time.sleep(0.5)

        # 솔벨브 Time 조정.
        Ardu.SetMaxTime('2000')
        time.sleep(0.5)

        # 솔벨브 On > 자동 Off 됨.
        Ardu.SetOutput(4, True)

        # 시린지 흡입 or 분주
        target_ul = int(self.ui.le_SP_TargetPos.text())
        SP.AbMovveSyringe(target_ul)    
        

    def SP_SolValveDispense(self):
        # maxtime 설정.
        maxtime_sol = self.ui.le_SV_MaxTime.text()
        Ardu.SetMaxTime(maxtime_sol)

        # 시린지 방향 B로 변경 파이펫 - 압력용기
        if SP.ChangeValveDir(2) == True:
            self.SP_UIChangeDirState(2)
        time.sleep(0.3)
        # 솔벨브 On > 자동 Off 됨.
        Ardu.SetOutput(4, True)
        time.sleep(2)
        Ardu.SetOutput(4, False)

    
    def SP_SetPulsePerUnit(self, pulseperunit):
        SP.pulseperunit = int(pulseperunit)

    def SP_Connect(self):
        comport = self.ui.cb_SP_Comport.currentText()
        SP.Connect(comport)
        time.sleep(1)
        if SP.IsConnected() == True:
            self.thread_SP_Monitoring.start()

    def SP_Home(self):
        # 시린지 방향 I로 변경
        if SP.ChangeValveDir(1) == True:
            self.SP_UIChangeDirState(1)
        time.sleep(0.5)

        # 솔벨브 Time 조정.
        Ardu.SetMaxTime('2000')
        time.sleep(0.5)

        # 솔벨브 On
        Ardu.SetOutput(4, True)

        # 시린지 Home
        SP.Home()
        time.sleep(1)
        self.SP_ChangeDir()

        # 솔벨브 Off
        Ardu.SetOutput(4, False)

    def SP_ChangeDir(self):
        value = self.ui.dial_Dir.value()
        if SP.ChangeValveDir(value) == True:
            self.SP_UIChangeDirState(value)
        time.sleep(0.5)

    def SP_UIChangeDirState(self, value):
        '''
            Z Initial 기준- I(1) = 파이펫,시린지, 
                            B(2) = 파이펫,압력용기, 
                            O(3) = 시린지, 압력용기
        '''
        dirstate = [] # 방향 상태 True = Open, False = Close
        self.ui.lb_SP_TopState.setText('') # 압력용기
        self.ui.lb_SP_BottomState.setText('') # 시린지
        self.ui.lb_SP_LeftState.setText('') # 파이펫

        if value == 1:
            dirstate = [False, True, True]
        elif value == 2:
            dirstate = [True, False, True]
        elif value == 3:
            dirstate = [True, True, False]
        if dirstate[0] == True: self.ui.lb_SP_TopState.setText('Open')
        if dirstate[1] == True: self.ui.lb_SP_BottomState.setText('Open')
        if dirstate[2] == True: self.ui.lb_SP_LeftState.setText('Open')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    apply_stylesheet(app, theme='dark_blue.xml')
    window.show()
    sys.exit(app.exec())


# ['dark_amber.xml',
#  'dark_blue.xml',
#  'dark_cyan.xml',
#  'dark_lightgreen.xml',
#  'dark_pink.xml',
#  'dark_purple.xml',
#  'dark_red.xml',
#  'dark_teal.xml',
#  'dark_yellow.xml',
#  'light_amber.xml',
#  'light_blue.xml',
#  'light_cyan.xml',
#  'light_cyan_500.xml',
#  'light_lightgreen.xml',
#  'light_pink.xml',
#  'light_purple.xml',
#  'light_red.xml',
#  'light_teal.xml',
#  'light_yellow.xml']