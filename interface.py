from operator import is_
import tkinter
import time
from datetime import timedelta

def start_clicked():
    global started
    global log
    global is_paused
    if is_paused:
        is_paused = False
        started = time.time()
        now = time.localtime(int(started))
        output_info = "started: " + str(time.strftime("%H:%M:%S", now))
        log.set(output_info)
        

def stop_clicked():
    global log
    global is_paused
    if not is_paused:
        is_paused = True
        elapsed = time.time() - started
        output_info = "elapsed: " + str(timedelta(seconds=elapsed))
        log.set(output_info)

is_paused = True
started = 0

app = tkinter.Tk()
app.geometry('180x240')

log = tkinter.StringVar()
log.set("00:00:00")

header = tkinter.Label(app, textvariable=log, fg="blue", font=("Arial Bold", 16))
header.pack(side="bottom", ipady=10)

starter = tkinter.Button(app, text="start", command= start_clicked)
starter.pack(side="top", ipady=10, ipadx=10, fill="x")


stop = tkinter.Button(app, text="stop and sync", command= stop_clicked)
stop.pack(side="top", ipady=10, ipadx=10, fill="x")

app.mainloop()