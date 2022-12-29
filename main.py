import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import time
import customtkinter

customtkinter.set_appearance_mode("light") 
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


app = customtkinter.CTk()
app.geometry("400x780")
app.title("EUR/USD")
#app.color='#FAEBD7'
plt.style.use(['Solarize_Light2'])
fig, ax = plt.subplots()
ax.plot(data['Date'], data['Close'])
ax.set_xlabel('Date')
ax.set_ylabel('Exchange rate')
def button_callback():
    print("Button click")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="x", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tk.LEFT)
label_1.pack(pady=10, padx=10)


button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
button_1.pack(pady=10, padx=10)

canvas = FigureCanvasTkAgg(fig, app)
canvas.get_tk_widget().pack(side='right', fill='y',ipadx=400)
app.mainloop()
