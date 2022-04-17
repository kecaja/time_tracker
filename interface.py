from operator import is_
import tkinter
import time

def start_clicked():
    global log
    global is_paused
    global started
    if is_paused:
        now = time.localtime(int(time.time()))
        output_info = "started: " + str(time.strftime("%H:%M:%S", now))
        log.set(output_info)
        is_paused = False

def pause_clicked():
    global log
    global is_paused
    if not is_paused:
        elapsed = 

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
# starter.grid(row=0, column=1)

pause = tkinter.Button(app, text="pause", command= start_clicked)
pause.pack(side="top", ipady=10, ipadx=10, fill="x")
# pause.grid(row=0, column=3)

stop = tkinter.Button(app, text="stop and sync", command= start_clicked)
stop.pack(side="top", ipady=10, ipadx=10, fill="x")

app.mainloop()