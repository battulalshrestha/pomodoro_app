'''import tkinter as tk 
from tkinter import messagebox
from ttkbootstrap import ttk, Style
WORK_TIME = 25 * 60
SHORT_BREAK_TIME= 5*60
LONG_BREAK_TIME = 15*60
class POmodoroTime:
    def __init__(self):
      self.root = tk.Tk()
      self.root.geometry('200x200')
      self.root.title("Pomodoro timer app")
      self.style = Style(theme="complex")
      self.style.theme_create()
      self.timer_label = tk.Label(self.root,text="",font=("TkDefaultFont",40))
      self.timer_label.pack(padx = 0,pady = 20)
      self.start_button = ttk.Button(self.root,text = "Start", command=self.start_time)
      self.stop_button = ttk.Button(self.root,text="stop",command=self.stop_time,state=tk.DISABLED)
      self.stop_button.pack(padx=0,pady=5)
      self.work_time = WORK_TIME
      self.break_time = SHORT_BREAK_TIME
      self.is_work_time,self.pomodoro_completed,self.is_running = True,0,False
      self.root.mainloop()
    def start_time(self):
      self.start_button.config(state = tk.DISABLED)
      self.stop_button.config(state = tk.NORMAL)
      self.is_running = True
      self.updat_time()
    def stop_time(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False
    def update_time(self):
        if self.is_running:
         if self.is_work_time:
            self.work_time-=1
            if self.work_time == 0:
                self.is_work_time = False
                self.pomodoro_completed += 1
                self.break_time = LONG_BREAK_TIME if self.pomodoro_completed % 4 == 0 else SHORT_BREAK_TIME
                messagebox.showinfo("you did great!" if self.pomodoro_completed %4 == 0
                else "take the long break and rest on to your mind"
                if self.pomodoro_completed % 4 == 0
                else "take the short break and stretch your lg!")
        else:
            self.break_time-= 1
            if self.break_time == 0:
                self.is_work_time,self.work_time = True,WORK_TIME
                messagebox.showinfo("work time","get back to the work!")
        minutes,seconds = divmod(self.work_time if self.is_work_time else self.break_time,60 )
        self.timer_label.config(text ="{:02d}:{:02d}".format(minutes,seconds))
        self.root.after(1000,self.update_time)
POmodoroTime()'''

from tkinter import *
import math
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import ttk, Style
# to set the time interval of the different work .
WORK_TIME = 3 * 10
SHORT_BREAK_TIME = 2 * 10
LONG_BREAK_TIME = 1 * 10
timer = None
# preparing the class for working task
class POmodoroTime:
    def __init__(self):
        # initialzing the tkinter as tk on the root button
        self.root = tk.Tk()
        #size of the display output layout 
        self.root.geometry('300x200')
        # setting the tittle
        self.root.title("Pomodoro Timer App")
   # giving the output of the style 
        self.style = Style(theme="simplex")
# setting the  timeer lable of the output 
        self.timer_label = tk.Label(self.root, text="", font=("", 50))
        # padding the timer lable of output horizontly and vertically by giving in padx and pady
        self.timer_label.pack(padx=0, pady=0)

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_time)
        self.start_button.pack(padx=5, pady=5)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_time, state=tk.DISABLED)
        self.stop_button.pack(padx=5, pady=5)

        self.reset_button = ttk.Button(self.root,text="Reset",command=self.reset_time)
        self.reset_button.pack(padx=5,pady=5)

        self.work_time = WORK_TIME
        self.break_time = SHORT_BREAK_TIME

        self.is_work_time = True
        self.pomodoro_completed = 0
        self.is_running = False
        
        self.root.mainloop()

    def start_time(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)
        self.is_running = True
        self.update_time()
    def reset_time(self):
        self.is_running = False
        self.work_time = WORK_TIME
        self.break_time = SHORT_BREAK_TIME
        self.timer_label.config(text = "00:00")

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        #self.reset_button.config(state=tk.NORMAL)
        # Tk.after_cancel(timer)
        # Canvas.itemconfig("timer_text",text= "00:00")

       
    def stop_time(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.is_running = False
        
    def update_time(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time -= 1
                if self.work_time == 0:
                    self.is_work_time = False
                    self.pomodoro_completed += 1
                    self.break_time = LONG_BREAK_TIME if self.pomodoro_completed % 4 == 0 else SHORT_BREAK_TIME
                    messagebox.showinfo("Great job!", "Take a long break!" if self.pomodoro_completed % 4 == 0 else "Take a short break!")
            else:
                self.break_time -= 1
                if self.break_time == 0:
                    self.is_work_time = True
                    self.work_time = WORK_TIME
                    messagebox.showinfo("Work time", "Get back to work!")

            minutes, seconds = divmod(self.work_time if self.is_work_time else self.break_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))

        self.root.after(1000, self.update_time)

POmodoroTime()
