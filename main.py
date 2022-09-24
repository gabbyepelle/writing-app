from tkinter import *
import math

timer = None
stop_writing_id = "id"


# ---------------------------- TIMER RESET ------------------------------- #
def start_timer():
    title.config(text="Don't Stop Typing!!!", fg="red")
    text_box.config(state=NORMAL)
    text_box.delete('1.0', END)
    start_button["state"] = "disabled"
    window.after(30000, stop_erasing)
    count_down(300)


def stop_erasing():
    text_box.config(state=DISABLED)
    start_button["state"] = "normal"
    title.config(text="Your masterpiece", fg="black")
    start_button.config(text="Start Again")


# ---------------------------- TEXT DELETE MECHANISM ------------------------------- #
def erase_text():
    text_box.delete('1.0', END)

def stop_writing(event):
    global stop_writing_id
    window.after_cancel(stop_writing_id)
    stop_writing_id = window.after(5000, erase_text)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_label.config(text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_label.config(text="00: 00")


# ----------------------------------UI SETUP------------------------------------#

window = Tk()
window.title("Disappearing Text Writing App")
window.configure(bg="white")
title = Label(text="Whatever you do, don't stop typing...")
title.config(font=("Futura", 40, "bold"), bg="white", pady=7, fg="black")
title.pack()
timer_label = Label(text="5:00")
timer_label.config(font=("Courier", 50, "bold"), bg="white", pady=10, fg="black")
timer_label.pack()

text_box = Text(window, height=20)
text_box.configure(font=("Courier", 40, "bold"), pady=20)
text_box.pack()

start_button = Button(text="Start", fg="black", bg="green", height=2, width=6, command=start_timer)
start_button.pack()

window.bind('<KeyRelease>', stop_writing)

window.mainloop()
