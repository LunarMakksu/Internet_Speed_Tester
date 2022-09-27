from os import times_result
import speedtest 
from datetime import datetime
import time
import multiprocessing as mp
import sys
import tkinter as tk
import matplotlib.pyplot as plt
from pandas import DataFrame as df
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

current_time = datetime.now().strftime("%H:%M:%S")
print('Propgram started at', current_time)
s = speedtest.Speedtest(secure=1)
global uploads
uploads = []
global downloads
downloads = []
global times_up, times_down
times_up = []
times_down = []
#global test_time
#test_time = int(input("How long would you like to run the test for? Please note that each data collection takes roughly 12 seconds to complete."))


def uptest():
    run = True
    telapse = 0
    n = 0
    while run == True:
        upload_test = round((round(s.upload()) / 1048576), 2) #converts to Mb/s
        uploads.append(upload_test)
        times_up.append(telapse)
        n += 1
        telapse += 12
        telapse = round(telapse,1)
        time.sleep(0.1)     
        if telapse == 10:
            run = False
            print("Upload data collected.")
            downtest()
        elif telapse < 10:
            run = True
        elif telapse > 10:
            print("there has been an error in the uptest runtime")
            run = False


def displaydata():
    root = tk.Tk()
    data1 = {'Time': times_up,
        'Upload_speed': uploads
        }
    df1 = df(data1,columns=['Time','Upload_speed'])

    data2 = {'Time': times_down,
            'Download_speed': downloads,
            } 
    df2 = df(data2, columns=['Time', 'Download_speed'])

    figure1 = plt.Figure(figsize=(5,4), dpi=100)
    ax1 = figure1.add_subplot(111)
    line1 = FigureCanvasTkAgg(figure1, root)
    line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['Time','Upload_speed']].groupby('Time').sum()
    df1.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
    ax1.set_title('Internet Upload Speed')

    figure2 = plt.Figure(figsize=(5,4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Time','Download_speed']].groupby('Time').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='g',marker='o', fontsize=10)
    ax2.set_title('Internet Download Speed')
    print("GUI launched.")
    root.mainloop()
   

def downtest():
    run = True
    telapse = 0
    n = 0
    while run == True:
        download_test = round((round(s.download()) / 1048576), 2)
        downloads.append(download_test)
        times_down.append(telapse)
        n += 1
        telapse += 0.2
        telapse = round(telapse,1)
        time.sleep(0.1)     
        if telapse == 10:
            run = False
            print("Download data collected.")
            time.sleep(2)
            displaydata()
        elif telapse < 10:
            run = True
        elif telapse > 10:
            print("there has been an error in the downtest runtime")
            run = False



print("Please wait for the program to collect data. Each data point takes roughly 12 seconds to collect.")
uptest()