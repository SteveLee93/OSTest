# Arduino Module 

import serial
import threading
import time
CMD_DI = 'di '
CMD_DO = 'do '
CMD_GET_IOSTATE = 'gio '
CMD_SET_MAXTIME = 'settime '
class Arduino():
    def __init__(self):
        global ser
        self._lock = threading.Lock()

    def Connect(self, comport):
        try:
            self.ser = serial.Serial(comport,9600)
            self.Log(f"Ardu {comport} Connected!!")
        except: 
            self.Log(f"Ardu {comport} Connect Fail!!")
    
    def IsConnected(self):
        try:
            return self.ser.is_open
        except:
            return False
    
    def Close(self):
        if self.IsConnected():
            self.ser.close()

    def Send(self, text):
        with self._lock:
            # send = bytearray(text.encode())
            try:
                send = str(f"{text}\r\n").encode()
                self.ser.write((f"{text}\r\n").encode())
                # self.ser.write(send)
                # print("-> ",send)
                time.sleep(0.5)
                try:
                    if self.ser.readable():                 # 수신 버퍼 체크
                        receive = self.ser.read_all()       # readline은 줄바꿈까지 읽는 듯?
                        # test = receive.decode()[:len(receive)]
                        # print(test)
                        return receive.decode()[:len(receive)]
                    else:
                        return 0
                except:
                    return 0
            except:
                return 0

    def SendOnly(self, text):
        with self._lock:
            # send = bytearray(text.encode())
            try:
                send = str(f"{text}\r\n").encode()
                self.ser.write((f"{text}\r\n").encode())
                # self.ser.write(send)
                # print("-> ",send)
                time.sleep(0.5)
            except:
                return 0

    def SetMaxTime(self, maxtime):
        # settime maxtime
        # result = self.Send(CMD_SET_MAXTIME + maxtime)
        result = self.SendOnly(CMD_SET_MAXTIME + maxtime)
        return result

    def GetInput(self, inputnum):
        result = self.Send(CMD_DI + str(inputnum))
        return result

    def SetOutput(self, outputnum, value):
        result = 0
        if value == True:
            # result = self.Send(CMD_DO + str(outputnum) + ' 1')
            result = self.SendOnly(CMD_DO + str(outputnum) + ' 1')
        else:
            # result = self.Send(CMD_DO + str(outputnum) + ' 0')
            result = self.SendOnly(CMD_DO + str(outputnum) + ' 0')
        
        self.Log(f"SetOutput outputnum = {outputnum}, value = {value}")
        return result

    def GetIOState(self, io_num):
        result = self.Send(CMD_GET_IOSTATE + str(io_num))
        # print(f"GetIOState result = {result}")
        return result
        
    def Log(self, log):
        '''
            log : 로그 내용
        '''
        print(f"Arduino Log : {log}")
