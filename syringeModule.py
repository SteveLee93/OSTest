# Syringe Pump Module

from ctypes.wintypes import CHAR
import serial
import time
import threading
from serial.tools.list_ports_windows import SetupDiOpenDevRegKey

# Command
CMD_END = 'R\r'
CMD_HOME = '/1Z' + CMD_END
CMD_ROTATE_I = '/1I' + CMD_END
CMD_ROTATE_O = '/1O' + CMD_END
CMD_ROTATE_B = '/1B' + CMD_END
# CMD_ROTATE_E = '/1E' + CMD_END
CMD_RELATIVE_DISPENCE = '/1D'
CMD_RELATIVE_ASPIRATE = '/1P'
CMD_APSOLUTE_MOVE = '/1A'
CMD_GET_CURRENTPOS = '/1?\r'
CMD_StartCharacter = b'/'
CMD_ETX = b'\x03'

class Syringe():
    def __init__(self):
        global ser
        self._lock = threading.Lock()

    def Close(self):
        if self.IsConnected():
            self.ser.close()

    @property
    def pulseperunit(self):
        return self._pulseperunit

    @pulseperunit.setter
    def pulseperunit(self, pulseperunit):
        self._pulseperunit = pulseperunit

    @property
    def velocity(self):
        return self._velocity
   
    @velocity.setter
    def velicity(self, velocity):  # 속도에 따른 스피드코드로 변환해줘야함 0~40사이 값의 코드.
        self._velocity = velocity

    def Connect(self, comport):
        try:
            self.ser = serial.Serial(comport,9600)
            self.Log(f"SP {comport} Connected!!")
        except:
            self.Log(f"SP {comport} Connect Fail!!")

    def IsConnected(self):
        try:
            return self.ser.is_open
        except:
            return False

    def Home(self):
        if(self.IsConnected() != True): return
        self.Send(CMD_HOME)

    def ChangeValveDir(self, value):
        '''
            Z Initial 기준- I(1) = 파이펫,시린지, 
                            B(2) = 파이펫,압력용기, 
                            O(3) = 시린지, 압력용기
        '''
        if(self.IsConnected() != True): return False

        if value == 1:
            direction = 'I'
            self.Send(CMD_ROTATE_I)
        elif value == 2:
            direction = 'B'
            self.Send(CMD_ROTATE_B)
        elif value == 3:
            direction = 'O'
            self.Send(CMD_ROTATE_O)
        self.Log(f"ChangeValveDir direction {direction} Done")
        return True

    def ReMoveSyringe(self, ul):
        '''
            현재 위치 기준으로 이동 - /1P숫자R pickup(aspirate), /1D숫자R dispense
        '''
        if(self.IsConnected() != True): return
        
        pulse = self.CalcUnitToPulse(ul)
        if ul > 0:
            self.Send(CMD_RELATIVE_ASPIRATE + str(pulse) + CMD_END)
        else:
            pulse *= -1
            self.Send(CMD_RELATIVE_DISPENCE + str(pulse) + CMD_END)

        self.Log(f"ReMoveSyringe ul = {ul} done")

    def AbMovveSyringe(self, target_ul):
        '''
            Target 위치로 이동  - /1A숫자R
        '''
        if(self.IsConnected() != True): return
        pulse = self.CalcUnitToPulse(target_ul)
        self.Send(CMD_APSOLUTE_MOVE + str(pulse) + CMD_END)

        self.Log(f"AbMovveSyringe target_ul = {target_ul} done")

    def CalcUnitToPulse(self, ul):
        '''
            ul to pulse 변환. 입력한 pulseperunit 만큼 곱해서 리턴.
        '''
        pulse_per_unit = self._pulseperunit
        pulse =int(ul / pulse_per_unit) 
        return pulse

    def GetCurPosition(self):
        try:
            if(self.IsConnected() != True): return 0
            pulse = int(self.Send(CMD_GET_CURRENTPOS))
            CurrentPosition = pulse * self.pulseperunit
            return CurrentPosition
        except:
            return 0

    def Log(self, log):
        '''
            log : 로그 내용
        '''
        print(f"Syringe Log : {log}")

    def Receive(self):
        response = ""
        try:
            response = self.ser.read_all()
        except Exception as e:
            print(e)
            print(type(e))
        return response
    
    def ClearBuffer(self):
        response = self.Receive()
        if response != b'':
            print(f"Clear Buffer <-- {response}")

    def Send(self, text):
        if self.IsConnected() != True: return
        with self._lock:
            self.ClearBuffer()
            send = bytearray(text.encode())
            self.ser.write(send)
            response = self.ReceiveUntilValidResponse()
            if self.IsError(response.decode()) == True: return
            # print("<- ", receive.decode()[:len(receive)-1])      # byte를 decode()로 string으로 변환
            result = []
            for x in response.decode()[:len(response)-1]:
                if x == '\x03':
                    break
                result.append(x)
            if len(result) > 2 :
                test = ''.join(result[3:])
            else:
                test = 0
            return test

    def ReceiveUntilValidResponse(self, msTimeout = 1000):
        response = ""
        timercount = 0  # 1ms counter
        while(True):
            response = self.Receive()
            if self.IsValidRespoense(response) == True: break
            if timercount > msTimeout:
                print(f"Recieve Timeout -- {msTimeout}ms")
                return ''
            time.sleep(0.1) # 100ms
            timercount += 100
        return response
    
    def IsValidRespoense(self, response):
        if response == b'': return False
        if response.index(CMD_StartCharacter) < 0: return False
        if response.index(CMD_ETX) < 0: return False
        return True

    def IsError(self, response):
        if len(response) == 0:
            print("response Length == 0")
            return True
        if len(response) <= 2: return False
        # statusByte = bytes(response[2])
        statusByte = response[2]
        errorByte = statusByte and b'0x0F'
        if errorByte == b'0x00' or errorByte == b'0x0F': return False

        #Error Case
        if errorByte == b'0x01': errorMessage = "Initialization failure"
        if errorByte == b'0x02': errorMessage = "Invalid command"
        if errorByte == b'0x03': errorMessage = "Invalid operand"
        if errorByte == b'0x04': errorMessage = "Invalid checksum"
        if errorByte == b'0x05': errorMessage = "Unused"
        if errorByte == b'0x06': errorMessage = "EEPROM failure"
        if errorByte == b'0x07': errorMessage = "Device not initialized"
        if errorByte == b'0x08': errorMessage = "CAN bus failure"
        if errorByte == b'0x09': errorMessage = "Plunger overload"
        if errorByte == b'0x0A': errorMessage = "Valve overload"
        if errorByte == b'0x0B': errorMessage = "Plunger move not allowed"
        if errorByte == b'0x0F': errorMessage = "Command overflow"

        print(errorMessage)
        return True



if __name__ == "__main__":
    # comport = 'COM3'
    # Connect(comport)
    pass

