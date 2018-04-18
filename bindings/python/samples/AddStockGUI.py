import stockConfig
from tkinter import *
from tkinter.colorchooser import *

color = ((255,255,255), '#ffffff')

def getColor():
    color = askcolor()
    

def addStock(editText):
    stock_text = editText.get()
    print("stock_text = " + str(stock_text))
    # stocks.append({"symbol":symbolField.get(), "red":color[0][0], "green":color[0][1], "blue":color[0][2]})
    # f = open("stockConfig.py", "w+")
    # f.write("stocks = ")
    # f.write(str(stockConfig.stocks))
    filename = "stockConfig.py"
    f = open(filename)

    stock_list = list(f)
    print("stock_list = " + str(stock_list))
    print("type(stock_list) = " + str(type(stock_list)))
    # try:
    #     for line in f:
    #         print(line),
    # finally:
    #     f.close()
    

stockList = stockConfig.stocks
master = Tk()
Label(master, text="Stock Symbol").grid(row=0)
symbolField = Entry(master)
symbolField.grid(row=0,column=1)
Button(text='Select Color', command=getColor).grid(row=1, column=1)
Button(text='Add Stock', command=lambda: addStock(symbolField)).grid(row=2, column=1)
mainloop()
