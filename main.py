import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import time

current_time = int(time.time())


start_time = current_time - 60*60*24*14  
end_time = current_time 
#chce brac dane z jakiego okresu ale nie dziala wiec zostawiam link bez zmian
data = pd.read_csv("https://query1.finance.yahoo.com/v7/finance/download/EURUSD=X?period1=1577836800&period2=1609459200&interval=1d&events=history")

window = tk.Tk()
window.title("EUR/USD Exchange Rate")

fig, ax = plt.subplots()

ax.plot(data['Date'], data['Close'])

ax.set_xlabel('Date')

ax.set_ylabel('Exchange rate')

canvas = FigureCanvasTkAgg(fig, window)
canvas.get_tk_widget().pack()

def button1_clicked():
    print("Button 1 clicked")

button1 = tk.Button(window, text="Button 1", command=button1_clicked)
button1.pack()

def button2_clicked():
    print("Button 2 clicked")

button2 = tk.Button(window, text="Button 2", command=button2_clicked)
button2.pack()

def button3_clicked():
    print("Button 3 clicked")

button3 = tk.Button(window, text="Button 3", command=button3_clicked)
button3.pack()

def button4_clicked():
    print("Button 4 clicked")

button4 = tk.Button(window, text="Button 4", command=button4_clicked)
button4.pack()

window.mainloop()