using rpi_rgb_led_matrix_sharp;
using System;
using System.Threading;

namespace font_example
{
    class Program
    {
        static int Main(string[] args)
        {
            if (args.Length < 1)
            {
                Console.WriteLine("font-example.exe [font_path] <text>");
                return -1;
            }
            string text = "abcdefghijklmnopqrstuvwxyz";
            string text_high = "AAPL 123.45";
            string text_low = "@ 12.4%";
            if (args.Length > 1)            
                text = args[1];
            

            var matrix = new RGBLedMatrix(16, 0, 0);
            var canvas = matrix.CreateOffscreenCanvas();
            var font = new RGBLedFont(args[0]);
 
	    var x = -40;
	    var top_y = 8;
	    var bot_y = 16;
		
	    	for(var j = 0; j < 1000; j++){
		    for(var i = 0; i < 80; i++){
			    x = x + 1;

			    // set all matrix low
			    canvas.Clear();

			    // draw the top line
		            canvas.DrawText(font, x, top_y, new Color(0, 255, 0), text_high);
		            canvas.DrawText(font, x, bot_y, new Color(0, 255, 0), text_low);

		            matrix.SwapOnVsync(canvas);

	                    Thread.Sleep(100);
			    
		
		            //while (!Console.KeyAvailable)
		            //{
		            //    Thread.Sleep(1000);
	            	    //}
	            	
	            }
		x = -40;
		top_y = 8;
		bot_y = 16;
		}

		/*
		// row test
		for(var i = 0; i < 1000; i++){
		    canvas.Clear();
			
	            canvas.DrawText(font, x, i, new Color(0, 255, 0), text);

	            matrix.SwapOnVsync(canvas);

                    Thread.Sleep(100);
		}
		*/


            return 0;
        }
    }
}
