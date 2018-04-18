import tkinter as tk
import shlex, subprocess
# import tkFont

print("HELLO")

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # tkFont.BOLD == 'bold'
        # helv36 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
        # command=lambda: callback(1)
        self.btn1 = tk.Button(text='ECHO', command=lambda: self.run_process('echo hello'))
        self.btn2 = tk.Button(text='LS', command=lambda: self.run_process('ls'))
        self.btn3 = tk.Button(text='python3 version', command=lambda: self.run_process('python3 --version'))
        self.btn4 = tk.Button(text='python2 version', command=lambda: self.run_process('python --version'))
        self.btn5 = tk.Button(text='btn5')

        self.btn1.pack(side="left")
        self.btn2.pack(side="left")
        self.btn3.pack(side="left")
        self.btn4.pack(side="left")
        self.btn5.pack(side="left")

    def say_hi(self):
        print("hi there, everyone!")

    def run_process(self, command):
        subprocess.run(command)


root = tk.Tk()
app = Application(master=root)
app.mainloop()