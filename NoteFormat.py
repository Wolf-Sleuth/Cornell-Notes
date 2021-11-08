import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import json
from functools import partial
import Menu


def main(filename: str = "*", title: str = "", key: str = "", notes: str = "", summary: str = ""):
    window = tk.Tk()
    window.title(filename)
    topFrame = tk.Frame(master=window)
    midFrame = tk.Frame(master=window)
    midFrameLeft = tk.Frame(master=midFrame, relief=tk.RAISED)
    midFrameRight = tk.Frame(master=midFrame, relief=tk.RAISED)
    midFrameLeft.grid(row=0, column=0)
    midFrameRight.grid(row=0, column=1)
    bottomFrame = tk.Frame(master=window)
    Title = tk.Entry(master=topFrame, width=100)
    Title.insert(tk.END, title)
    Key = tk.Text(master=midFrameLeft, width=25, height=40)
    Key.insert(tk.END, key)
    Notes = tk.Text(master=midFrameRight, width=75, height=40)
    Notes.insert(tk.END, notes)
    Summary = tk.Text(master=bottomFrame, width=100, height=10)
    Summary.insert(tk.END, summary)
    savebtn = tk.Button(master = window, text="Save", command=partial(
        save, 
        filename, 
        Title, 
        Key, 
        Notes, 
        Summary
    ))
    openbtn = tk.Button(master = window, text="Open New", command=partial(open, window))
    topFrame.pack()
    midFrame.pack()
    bottomFrame.pack()
    Title.pack()
    Key.pack()
    Notes.pack()
    Summary.pack()
    savebtn.pack()
    openbtn.pack()
    window.mainloop()

def save(filename, Title, Key, Notes, Summary):
    # Code for saving stuff here.
    file = {
        "Filename":filename,
        "Title":(Title.get()),
        "Key":(Key.get(1.0, tk.END)),
        "Notes":(Notes.get(1.0, tk.END)),
        "Summary":(Summary.get(1.0, tk.END))
    }
    if file["Filename"] == "*":
        filepath = asksaveasfilename(
        defaultextension="CoNo",
        filetypes=[("Cornell Files", "*.CoNo"), ("All Files", "*.*")],
    )
        if not filepath:
            print("not filepath")
            return
    else:
        filepath = file["Filename"]
    file["Filename"] = filepath
    with open(filepath, "w") as notesFile:
        json.dump(file, notesFile)


def open(window):
    window.destroy()
    Menu.main()


if __name__ == "__main__":
    main("*", "hello", "hello\nhow are you", "hello", "hello")