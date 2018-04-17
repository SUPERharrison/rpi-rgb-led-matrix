#!/usr/bin/env python
# Display a runtext with double-buffering.\
# -*- coding: utf-8 -*-
from samplebase import SampleBase
from rgbmatrix import graphics
from decimal import Decimal
from datetime import date, timedelta
import time
import intrinio
import stockConfig


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()

        # load the font displayed to screen (letter dimension
        font.LoadFont("../../../fonts/5x8.bdf")
        pos = offscreen_canvas.width

        # important data for accessing the stock API (pulls information)
        intrinio.client.username = ''
        intrinio.client.password = ''

        # get the yesterday
        yesterday = date.today() - timedelta(7)
        dateCheck = yesterday.strftime("%Y-%m-%d");

        # print the current date
        print("dateCheck = " + str(dateCheck))

        # list to hold stocks
        stockdata = []

        # list to hold the percentage change
        changedata = []

        # list to hold colors of the stock
        stockcolors = []

        # list to hold color of percent
        percentcolors = []

        # loop thru the stocks listed in
        for i in stockConfig.stocks:
            # get value for current day (today)
            value = intrinio.prices(i['symbol'], dateCheck) 
            stock_text = i['symbol']
            stock_text = stock_text + ' ' + str(value.iloc[0][5])
            stockdata.append(stock_text)

            stockColor = graphics.Color(i['red'], i['green'], i['blue'])
            stockcolors.append(stockColor)
            
            percentChange = ((value.iloc[0][5] - value.iloc[0][9]) / value.iloc[0][5]) * 100
            if (percentChange < 0):
                percent_text = '∇'
                percentColor = graphics.Color(255,0,0)
            elif (percentChange > 0):
                percent_text = 'Δ'
                percentColor = graphics.Color(0,255,0)
            else:
                percentColor = graphics.Color(0,0, 255)
            
            percent_text = percent_text + str(abs(round(Decimal(percentChange), 2)))
            percent_text = (' ' * (len(stock_text) - len(percent_text))) + percent_text
            changedata.append(percent_text)
            percentcolors.append(percentColor)
            
        currentStock = 0
        
        while True:

            offscreen_canvas.Clear()
            length = graphics.DrawText(offscreen_canvas, font, pos, 7, stockcolors[currentStock], stockdata[currentStock])
            len2 = graphics.DrawText(offscreen_canvas, font, pos, 14, percentcolors[currentStock], changedata[currentStock])
            pos -= 1
            if (pos + length < 0):
                pos = offscreen_canvas.width
                currentStock += 1
                if(currentStock >= len(stockdata)):
                    currentStock = 0

            time.sleep(0.07)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
