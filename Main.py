import tkinter as tk
import os
import sys



window = tk.Tk()
window.title("Cornell Notes")
topFrame = tk.Frame(master=window)
midFrame = tk.Frame(master=window)
midFrameLeft = tk.Frame(master=midFrame, relief=tk.RAISED)
midFrameRight = tk.Frame(master=midFrame, relief=tk.RAISED)
midFrameLeft.grid(row=0, column=0)
midFrameRight.grid(row=0, column=1)
bottomFrame = tk.Frame(master=window)
Title = tk.Entry(master=topFrame, width=100)
Key = tk.Text(master=midFrameLeft, width=25, height=40)
Notes = tk.Text(master=midFrameRight, width=75, height=40)
Summary = tk.Text(master=bottomFrame, width=100, height=10)
topFrame.pack()
midFrame.pack()
bottomFrame.pack()
Title.pack()
Key.pack()
Notes.pack()
Summary.pack()
window.mainloop()