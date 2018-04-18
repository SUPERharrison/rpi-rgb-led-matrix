import stockConfig
from tkinter import *
from tkinter.colorchooser import *

color = ((255,255,255), '#ffffff')

def getColor():
    color = askcolor()
    

def addStock(stocks, symbol):
    stocks.append({"symbol":symbolField.get(), "red":color[0][0], "green":color[0][1], "blue":color[0][2]})
    f = open("stockConfig.py", "w+")
    f.write("stocks = ")
    f.write(str(stockConfig.stocks))
    

stockList = stockConfig.stocks
master = Tk()
Label(master, text="Stock Symbol").grid(row=0)
symbolField = Entry(master)
symbolField.grid(row=0,column=1)
Button(text='Select Color', command=getColor).grid(row=1, column=1)
Button(text='Add Stock', command=addStock(stockList, symbolField)).grid(row=2, column=1)
mainloop()
