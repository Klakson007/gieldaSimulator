import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import time
import customtkinter

customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("blue")
current_time = int(time.time())
start_time = current_time - 60*60*24*14  
end_time = current_time 

#chce brac dane z jakiego okresu ale nie dziala wiec zostawiam link bez zmian
data = pd.read_csv("https://query1.finance.yahoo.com/v7/finance/download/EURUSD=X?period1=1577836800&period2=1609459200&interval=1d&events=history")
'''
window = tk.Tk()
window.title("EUR/USD Exchange Rate")
#window['background']='#FAEBD7'
plt.style.use(['Solarize_Light2'])
fig, ax = plt.subplots()
ax.plot(data['Date'], data['Close'])
ax.set_xlabel('Date')
ax.set_ylabel('Exchange rate')

canvas = FigureCanvasTkAgg(fig, window)
canvas.get_tk_widget().pack(side='right', fill='y',ipadx=400)
window.mainloop()
'''
self.title("CustomTkinter complex_example.py")
self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
self.grid_columnconfigure(1, weight=1)
self.grid_columnconfigure((2, 3), weight=0)
self.grid_rowconfigure((0, 1, 2), weight=1)
