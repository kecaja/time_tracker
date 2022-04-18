try:
    from logging import exception
    from operator import is_
    import tkinter
    import time
    from datetime import timedelta

    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    import pandas as pd
except:
     print("can't load all packages")

is_paused = True
started = 0
ended = 0
elapsed = 0


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
    global ended
    global elapsed
    global is_paused
    if not is_paused:
        is_paused = True
        ended = time.time()
        elapsed = time.time() - started
        output_info = "elapsed: " + str(timedelta(seconds=round(elapsed,0)))
        log.set(output_info)
        try:
            write_to_drive()
            # time.sleep(3)
            # quit()
        except:
            print('last error')
            quit()

def sync():
    is_paused = True

def write_to_drive():
    global started
    global ended
    global elapsed
    
    try:
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
        drive = GoogleDrive(gauth)
    except:
            print("authentification error")
    try:
        fileDownloaded = drive.CreateFile({'id':'1zTuFXiai6eyDbejX1tyKt9B6phYUEj_C'})
        fileDownloaded.GetContentFile('data.csv')
    except:
        print("can't open the file")

    try:
        myCsvRow = str(time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(int(started)))) + ';' + str(time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(int(ended)))) + ';'+ str(timedelta(seconds=round(elapsed,0))) + '\n'
        with open('data.csv','a') as fd:
            fd.write(myCsvRow)
        fileDownloaded.SetContentFile(f'data.csv')
        fileDownloaded.Upload()
        print('file uploaded successfully')
    except:
        print('error opening the file')
        quit()






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