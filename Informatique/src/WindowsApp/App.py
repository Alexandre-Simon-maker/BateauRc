import serial
from tkinter import *
from tkinter import ttk

class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)

        self.port = Label(self, text="Port:")
        self.baudRate = Label(self, text="Baud Rate:")
        self.comboBoxPorts = ttk.Combobox(self)
        self.comboBoxBaudRate = ttk.Combobox(self)
        self.connect = Button(self, text = "Connect device", command=self.connectDevice)
        self.port.grid(row = 0, column = 0, pady = 2)
        self.baudRate.grid(row = 1, column = 0, pady = 2)
        self.comboBoxPorts.grid(row = 0, column = 1, pady = 2)
        self.comboBoxBaudRate.grid(row = 1, column = 1, pady = 2)
        self.connect.grid(row = 2, column = 0, columnspan = 2)

    #     self.createWidget()
    #     #self.initializeLists()
    #     #self.startMarker = 60
    #     #self.endMarker = 62
    #     #self.ser = None

    # def createWidget(self):
    #     self.port = Label(self, text="Port:")
    #     self.baudRate = Label(self, text="Baud Rate:")
    #     self.comboBoxPorts = ttk.Combobox(self)
    #     self.comboBoxBaudRate = ttk.Combobox(self)
    #     self.connect = Button(self, text = "Connect device", command=self.connectDevice)
    #     self.port.grid(row = 0, column = 0, pady = 2)
    #     self.baudRate.grid(row = 1, column = 0, pady = 2)
    #     self.comboBoxPorts.grid(row = 0, column = 1, pady = 2)
    #     self.comboBoxBaudRate.grid(row = 1, column = 1, pady = 2)
    #     self.connect.grid(row = 2, column = 0, columnspan = 2)
    
    # def initializeLists(self):
    #     listPort = []
    #     listPort.append("COM1")
    #     listPort.append("COM2")
    #     listPort.append("COM3")
    #     listPort.append("COM4")
    #     listPort.append("COM5")

    #     listBaudRate = []
    #     listBaudRate.append(9600)
    #     listBaudRate.append(115200)
    #     self.comboBoxPorts['values'] = listPort
    #     self.comboBoxBaudRate['values'] = listBaudRate

    def connectDevice(self):
        self.waitArduino()

    # def sendToArduino(self, sendStr):
    #     self.ser.write(self.sendStr.encode())

    # def recvFromArduino(self):
    #     ck = ""
    #     x = "z"
    #     byteCount = -1
    #     while ord(x) != self.startMarker: 
    #         x = ser.read()

        
    #     while ord(x) != self.endMarker:
    #         if ord(x) != self.startMarker:
    #             ck = ck + x.decode("utf-8")
    #             byteCount += 1
    #         x = ser.read()
                
    #     return(ck)

    # def waitArduino(self):
    #     msg = ""
    #     while msg.find("Arduino ready") == -1:
    #         while self.ser.inWaiting() == 0:
    #             pass

    #         msg = self.recvFromArduino()
    #         print(msg)
    #         print

#------------------------
# Main part of programm
#------------------------

fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()


# serPort = "COM5"
# baudRate = 9600
# ser = serial.Serial(serPort, baudRate)
# print("Serial port " + serPort + " opened / Baudrate " + str(baudRate))