from reminder import *
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.title("Reminders")


def reminder():
    title = simpledialog.askstring("Make Reminder", "Reminder Name?")
    message = simpledialog.askstring("Make Reminder", "Reminder Description?")
    tm = simpledialog.askinteger("Make Reminder", "In How Many Minutes?")

    visual = tk.Label(frame, text = title, bg = "white")
    visual.pack()
    root.after(1000 * tm, visual.destroy)
    root.after(1000 * tm, setReminder, title, message)


board = tk.Canvas(root, width=800, height=600, bg="black")
board.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

newReminder = tk.Button(root, text="New Reminder", padx=10, pady=5,
                        fg="black", bg="white", command = reminder)
newReminder.pack()

root.mainloop()