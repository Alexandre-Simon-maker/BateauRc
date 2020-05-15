import tkinter as tk
from tkinter import ttk
import serial

class MenuStart(tk.Frame):
    def __init__(self, arduino_, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widget_list = []
        self.create_widgets()
        self.initializeList()
        self.arduino = arduino_

    def create_widgets(self):
        self.port = tk.Label(self, text="Port:")
        self.baudRate = tk.Label(self, text="Baud Rate:")
        self.comboBoxPorts = ttk.Combobox(self, state='readonly')
        self.comboBoxBaudRate = ttk.Combobox(self, state='readonly')
        self.connect = tk.Button(self, text = "Connect device", command= lambda: arduino.connectDevice(self.comboBoxPorts.get(), self.comboBoxBaudRate.get()))
        self.nextPage = tk.Button(self, text = "Next page", command=self.master.destroy)

        self.widget_list.append(self.port)
        self.widget_list.append(self.baudRate)
        self.widget_list.append(self.comboBoxPorts)
        self.widget_list.append(self.comboBoxBaudRate)
        self.widget_list.append(self.connect)
        self.widget_list.append(self.nextPage)


        self.port.grid(row = 0, column = 0, pady = 2)
        self.baudRate.grid(row = 1, column = 0, pady = 2)
        self.comboBoxPorts.grid(row = 0, column = 1, pady = 2)
        self.comboBoxBaudRate.grid(row = 1, column = 1, pady = 2)
        self.connect.grid(row = 2, column = 0, pady = 2)
        self.nextPage.grid(row = 2, column = 1, pady = 2)

    def initializeList(self):
        self.comboBoxPorts['values'] = ["COM1", "COM2", "COM3", "COM4", "COM5"]
        self.comboBoxPorts.current(4)
        self.comboBoxBaudRate['values'] = ["9600", "115200"]
        self.comboBoxBaudRate.current(0)

class Application(tk.Frame):
    def __init__(self, arduino_, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.arduino = arduino_
        self.ledStates = [False, False, False, False, False, False]

    def create_widgets(self):
        self.led1 = tk.Button(self, text = "Led1", bg='white', command= lambda: self.sendCommand(1))
        self.led1.grid(row = 0, column = 0, pady = 2)
        self.led2 = tk.Button(self, text = "Led2", bg='white', command= lambda: self.sendCommand(2))
        self.led2.grid(row = 1, column = 0, pady = 2)
        self.led3 = tk.Button(self, text = "Led3", bg='white', command= lambda: self.sendCommand(3))
        self.led3.grid(row = 2, column = 0, pady = 2)
        self.led4 = tk.Button(self, text = "Led4", bg='white', command= lambda: self.sendCommand(4))
        self.led4.grid(row = 3, column = 0, pady = 2)
        self.led5 = tk.Button(self, text = "Led5", bg='white', command= lambda: self.sendCommand(5))
        self.led5.grid(row = 4, column = 0, pady = 2)
        self.led6 = tk.Button(self, text = "Led6", bg='white', command= lambda: self.sendCommand(6))
        self.led6.grid(row = 5, column = 0, pady = 2)
        self.buttonQuit = tk.Button(self, text = "Quit", command=self.quitApplication)
        self.buttonQuit.grid(row = 6, column = 0, pady = 10)

    def sendCommand(self, ledNumber):
        if self.ledStates[ledNumber - 1] == True:
            self.ledStates[ledNumber - 1] = False
            command = "<LED" + str(ledNumber) + ",L>"
            arduino.sendToArduino(command)
        else:
            self.ledStates[ledNumber - 1] = True
            command = "<LED" + str(ledNumber) + ",H>"
            arduino.sendToArduino(command)

    def quitApplication(self):
        arduino.closeSerial()
        self.master.destroy()

class Arduino:
    def __init__(self):
        self.ser = None
        self.endMarker = 62
        self.startMarker = 60

    def connectDevice(self, port, baudRate):
        self.ser = serial.Serial(port, int(baudRate))
        print("Serial port " + port + " opened / Baudrate " + baudRate)
        self.waitArduino()

    def waitArduino(self):
        msg = ""
        while msg.find("Arduino ready") == -1:
            while self.ser.inWaiting() == 0:
                pass

            msg = self.recvFromArduino()
            print(msg)
            print

    def recvFromArduino(self):
        ck = ""
        x = "z"
        byteCount = -1
        while ord(x) != self.startMarker: 
            x = self.ser.read()

        
        while ord(x) != self.endMarker:
            if ord(x) != self.startMarker:
                ck = ck + x.decode("utf-8")
                byteCount += 1
            x = self.ser.read()
                
        return(ck)

    def sendToArduino(self, sendstr):
        self.ser.write(sendstr.encode())

    def closeSerial(self):
        self.ser.close()


arduino = Arduino()
startFenetre = tk.Tk()
start = MenuStart(arduino, master=startFenetre)
start.mainloop()

appFenetre = tk.Tk()
app = Application(arduino,master=appFenetre)
app.mainloop()