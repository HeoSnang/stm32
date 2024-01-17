import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import re

ser=serial.Serial("COM12", 115200)

fig, ax=plt.subplots()
data1=deque(maxlen=100)
data2=deque(maxlen=100)
bar1=ax.bar(0, 0, width=10)
bar2=ax.bar(30, 0, width=10)

ax.set_aspect('equal')

def update_graph(frame):
    if ser.in_waiting>0:
        line=ser.readline().decode("utf-8").rstrip()
        try:
            number_string = re.findall(r"\d+", line)
            number_int = [int(num) for num in number_string]
            # data store
            data1.append(number_int[0])
            data2.append(number_int[1])
            ax.clear()
            ax.plot(data1, color='red')
            ax.plot(data2, color='blue')
            
        except ValueError:
            pass
def update_bar(frame):
    if ser.in_waiting > 0:
        line=ser.readline().decode("utf-8").rstrip()
        try:
            #data paser
            number_string = re.findall(r"\d+", line)
            number_int = [int(num) for num in number_string]
            #data store
            bar1[0].set_height(number_int[0])
            bar2[0].set_height(number_int[1])
            
            ax.set_ylim(0,100)
        except ValueError:
            pass

def update_pie(frame):
    if ser.in_waiting > 0:
        line= ser.readline().decode("utf-8"). rstrip()
        try:
            #data paser
            number_string = re.findall(r"\d+", line)
            number_int = [int(num) for num in number_string]
            #data store
            ax.clear()
            ax.pie([number_int[0], number_int[1]], startangle = 90,counterclock=False, colors=['blue', 'gray'])
        except ValueError:
            pass
ani=animation.FuncAnimation(fig, update_pie, interval=1)
plt.show()

ser.close()


#온도, 습도 결과값 도출
#import serial
#ser=serial.Serial("COM3", 115200)
#while True:
#    if ser.in_waiting>0:
#        data=ser.readline().decode("utf-8").rstrip()
        #rstrip을 빼면 출력이 줄 바꿈
#        print(data)
