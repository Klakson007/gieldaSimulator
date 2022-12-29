import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import time
import customtkinter

customtkinter.set_appearance_mode("dark") 
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
app.config(background='#FAEBD7')
#app.color='#FAEBD7'
plt.style.use(['Solarize_Light2'])
fig, ax = plt.subplots()
ax.plot(data['Date'], data['Close'])
ax.set_xlabel('Date')
ax.set_ylabel('Exchange rate')
def button_callback():
    print("Button click")

frame_1 = customtkinter.CTkFrame(master=app,fg_color='#e6d5be',bg_color='#e6d5be').place(x=11110,y=0)
frame_1.pack(fill="x", expand=True,side='left')

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback,fg_color='#fc0808',height=80,width=160)
button_1.pack(pady=5, padx=5,side='left',expand=True)
button_2 = customtkinter.CTkButton(master=frame_1, command=button_callback,fg_color='#384ef5',height=80,width=160)
button_2.pack(pady=5, padx=5,side='right',expand=True)

canvas = FigureCanvasTkAgg(fig, app)
canvas.get_tk_widget().pack(side='right', fill='y',ipadx=400)
app.mainloop()
