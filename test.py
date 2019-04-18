from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
from ctypes import *
FTDI = CDLL("./main.dll") #Importing C functions for FTDI interfacing
x_data, y_data = [], []
handle = FTDI.interfacing()
figure = pyplot.figure()
line, = pyplot.plot_date(x_data, y_data, '-')

def update(frame):
    raw = FTDI.working(handle)
    voltage = raw*0.01953 #multiplying digital readings by step size of ADC
    try: #circumventing Active Low default pin state which would give 5V reading at 0V
       if (y_data[-1] <0.2 and y_data[-1]>0 and voltage >4.8):
          voltage = 0.1
    except IndexError as e:
        print("ok")
    x_data.append(datetime.now())
    y_data.append(voltage)
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,

animation = FuncAnimation(figure, update, interval=200)

pyplot.show()