import serial
from tkinter import *

def funPlay():
    ser.write(bytes(b'cdefgabCdfabCegC'))

def funStop():
    ser.write(bytes(b' '))

def fun_c():
    ser.write(bytes(b'c'))
def fun_d():
    ser.write(bytes(b'd'))
def fun_e():
    ser.write(bytes(b'e'))
def fun_f():
    ser.write(bytes(b'f'))
def fun_g():
    ser.write(bytes(b'g'))
def fun_a():
    ser.write(bytes(b'a'))
def fun_b():
    ser.write(bytes(b'b'))
def fun_C():
    ser.write(bytes(b'C')) 
ser=serial.Serial("COM12", 115200)

win = Tk()
win.geometry("500x300")
label = Label(win, text="STM32 MCU Piano")
bPlay = Button(win, text="재생",command=funPlay)
bStop = Button(win, text="정지",command=funStop)
bDo = Button(win, text="도", command=fun_c)
bRe = Button(win, text="레", command=fun_d)
bMi = Button(win, text="미", command=fun_e)
bPa = Button(win, text="파", command=fun_f)
bSo = Button(win, text="솔", command=fun_g)
bLa = Button(win, text="라", command=fun_a)
bSi = Button(win, text="시", command=fun_b)
bDO = Button(win, text="도", command=fun_C)
label.pack()
#bStop.pack(padx=10, pady=10)
#bPlay.pack(padx=10, pady=10)
bStop.place(x=200, y=20)
bPlay.place(x=20, y=40)
bDo.place(x=20, y=60)
bRe.place(x=100, y=60)
bMi.place(x=180, y=60)
bPa.place(x=260, y=60)
bSo.place(x=340, y=60)
bLa.place(x=420, y=60)
bSi.place(x=20, y=100)
bDO.place(x=100, y=100)

win.mainloop()
