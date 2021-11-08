import tkinter as tk
from tkinter.filedialog import askopenfilename
import NoteFormat
import json
from functools import partial


def open_file(window):
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Cornell Files", "*.CoNo"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    # Put a call to the code used to edit files here
    with open(filepath, "r") as notesFile:
        notes = json.loads(notesFile.read())
    window.destroy()
    NoteFormat.main(
        notes["Filename"],
        notes["Title"],
        notes["Key"],
        notes["Notes"],
        notes["Summary"])

def new_file(window):
    window.destroy()
    NoteFormat.main()


def main():
    window = tk.Tk()
    window.title("Cornell Notes")
    btn_new = tk.Button(window, text="New File", command=partial(new_file, window))
    btn_open = tk.Button(window, text="Open File", command=partial(open_file, window))
    btn_new.pack()
    btn_open.pack()
    window.mainloop()


if __name__ == "__main__":
    main()