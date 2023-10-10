import time
import tkinter as tk
from tkinter import messagebox
import pygame

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        timer_label.config(text=timeformat)
        root.update()
        time.sleep(1)
        seconds -= 1

    timer_label.config(text="Time's up!")
    play_sound()

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm1.wav")  # Replace "sound.wav" with your sound file
    pygame.mixer.music.play()

def start_timer():
    try:
        user_input = int(entry.get())
        countdown_timer(user_input)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of seconds.")

root = tk.Tk()
root.title("Countdown Timer")

entry_label = tk.Label(root, text="Enter the countdown time in seconds:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

timer_label = tk.Label(root, text="", font=("Helvetica", 48))
timer_label.pack()

root.mainloop()
