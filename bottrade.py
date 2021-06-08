import tkinter as tk
from tkinter import *
import tkinter
from PIL import Image
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import yfinance as yf
from PIL import Image, ImageTk
import os

#Data viz
import plotly.graph_objs as go
def btcchart():
    data = yf.download(tickers='BTC-USD', period = '22h', interval = '15m')
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))
    fig.update_layout(
    title='Bitcoin live share price evolution',
    yaxis_title='Bitcoin Price (kUS Dollars)')
    fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=6, label="6h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
     )
    )
    fig.show()
def Dogec():
    data = yf.download(tickers='DOGE-USD', period = '22h', interval = '15m')
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))
    fig.update_layout(
    title='Doge live share price evolution',
    yaxis_title='Doge Price (kUS Dollars)')
    fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=6, label="6h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
     )
    )
    fig.show()
def ethc():
    data = yf.download(tickers='ETH-USD', period = '22h', interval = '15m')
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))
    fig.update_layout(
    title='ETH live share price evolution',
    yaxis_title='ETH Price (kUS Dollars)')
    fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=6, label="6h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
     )
    )
    fig.show()
def bnbc():
    data = yf.download(tickers='BNB-USD', period = '22h', interval = '15m')
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))
    fig.update_layout(
    title='BNB live share price evolution',
    yaxis_title='BNB Price (kUS Dollars)')
    fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=6, label="6h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
     )
    )
    fig.show()

def btcpri():
    root = tkinter.Toplevel()
    
    img = ImageTk.PhotoImage(Image.open("sitpri.png"))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    root.mainloop()

# Create a photoimage object of the image in the path
def dogepri():
     root = tkinter.Toplevel()
    
     img = ImageTk.PhotoImage(Image.open("dogepri.PNG"))
     panel = Label(root, image = img)
     panel.pack(side = "bottom", fill = "both", expand = "yes")
     root.mainloop()

    
def ethpri():
    root = tkinter.Toplevel()
    
    img = ImageTk.PhotoImage(Image.open("ETH Pri.PNG"))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    root.mainloop()
def bnbpri():
    root = tkinter.Toplevel()
    
    img = ImageTk.PhotoImage(Image.open("BNBpri.PNG"))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    root.mainloop()



    
    
    


    
    



window=Tk()
# add widgets here
btcP = PhotoImage(file='D:\ฝึกjava\pt1.png')
dogP = PhotoImage(file='D:\ฝึกjava\dogecoin.png')
ethp = PhotoImage(file='D:\ฝึกjava\ethp.png')
bnbp = PhotoImage(file='D:\ฝึกjava\sbnb.png')
qrcode = PhotoImage(file='D:\ฝึกjava\qrcode.PNG')
img = ImageTk.PhotoImage(Image.open('D:\ฝึกjava\qrre.png'))
panel = tk.Label(window, image = img)
panel.place(x=400,y=400)
window.title(' V1 by Title')
window.geometry("500x500+10+20")
window.configure(bg='Black')


but1 = Button(window,text="BTC",bd=5,bg='Black',image=btcP,command=btcchart)
but1.place(x=25,y=100)
but2 = Button(window,text="DOGE",bd=5,bg='Black',image=dogP,command=Dogec)
but2.place(x=25,y=200)
but3 = Button(window,text="ETH",bd=5,bg='Black',image=ethp,command=ethc)
but3.place(x=25,y=300)
but4 = Button(window,text="BNB",bd=5,bg='Black',image=bnbp,command=bnbc)
but4.place(x=25,y=400)
butp1 = Button(window,text="PREDIC BTC",bd=5,bg='WHITE',command=btcpri)
butp1.place(x=200,y=100)
butp2 = Button(window,text="PREDIC DOGE",bd=5,bg='WHITE',command=dogepri)
butp2.place(x=200,y=200)
butp3 = Button(window,text="PREDIC ETH",bd=5,bg='WHITE',command=ethpri)
butp3.place(x=200,y=300)
butp4 = Button(window,text="PREDIC BNB",bd=5,bg='WHITE',command=bnbpri)
butp4.place(x=200,y=400)
window.mainloop()