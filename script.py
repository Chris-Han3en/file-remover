import tkinter as tk, os, sys
from tkinter import messagebox

root = tk.Tk()

canvas1 = tk.Canvas(
    root,
    width=300,
    height=300,
)  # the size of the main screen
canvas1.pack()


def application():
    MsgBox = tk.messagebox.askquestion(
        "START SCRIPT",
        'Are you sure you want to start the script, there is no going back.',
        icon="warning",
    )
    if MsgBox == "yes":  # if user selected yes
        for r, d, f in os.walk("D:\\"):  # what drive it searches
            for files in f:
                if files == "RainbowSix.exe":  # file it is looking for
                    location = os.path.join(r, files)  # finds the location of the file
                    print(location)  # prints the location (mostly for dev purposes)
                    if os.path.exists(location):
                        os.remove(location)  # removes the file
    else:
        tk.messagebox.showinfo(
            "PUSSY", "You will now return to the application screen"
        )  # sends them back to the main screen


button1 = tk.Button(
    root, text="START SCRIPT", command=application, bg="red", fg="black"
)  # displays the run button
canvas1.create_window(
    150,
    150,
    window=button1,
)  # creates button

root.mainloop()
