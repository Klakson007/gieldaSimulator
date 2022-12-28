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
#window.attributes('-fullscreen',True)
window.title("EUR/USD Exchange Rate")
window['background']='#151B54'
fig, ax = plt.subplots()

ax.plot(data['Date'], data['Close'])

ax.set_xlabel('Date')

ax.set_ylabel('Exchange rate')

canvas = FigureCanvasTkAgg(fig, window)
canvas.get_tk_widget().pack()
window.mainloop()