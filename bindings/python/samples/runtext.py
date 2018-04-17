#!/usr/bin/env python
# Display a runtext with double-buffering.\
# -*- coding: utf-8 -*-
from samplebase import SampleBase
from rgbmatrix import graphics
from decimal import Decimal
import time
import intrinio


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/5x8.bdf")
        stockColor = graphics.Color(0, 50, 255)
        pos = offscreen_canvas.width

        intrinio.client.username = '8f8b30cbd435e8b001cd4ef0c3e23635'
        intrinio.client.password = '2ff6afdc9c1ad05a93a08776c0bbff92'

        value = intrinio.prices('GOOGL', start_date='2018-04-13')
        stock_text = 'GOOGL '
        stock_text = stock_text + str(value.iloc[0][5])
        
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

        
        while True:
            offscreen_canvas.Clear()
            length = graphics.DrawText(offscreen_canvas, font, pos, 7, stockColor, stock_text)
            len2 = graphics.DrawText(offscreen_canvas, font, pos, 14, percentColor, percent_text)
            pos -= 1
            if (pos + length < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
