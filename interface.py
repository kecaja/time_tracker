try:
    from logging import exception
    from operator import is_
    import tkinter
    import time
    from datetime import timedelta

    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

except:
     print("can't load all packages")

is_paused = True
started = 0
ended = 0
elapsed = 0

def show_error(text):
    tkinter.messagebox.showerror('Error', text)


def start_clicked():
    global app
    global started
    global log
    global is_paused
    if is_paused:
        is_paused = False
        started = time.time()
        now = time.localtime(int(started))
        output_info = "started: " + str(time.strftime("%H:%M:%S", now))
        log.set(output_info)
        app.after(1000,set_label)
        
def set_label():
    global started
    if not is_paused:    
        elapsed = time.time() - started
        output_info = str(timedelta(seconds=round(elapsed,0)))
        elapsed_time.set(output_info)
        app.after(1000,set_label)

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
        elapsed_time.set(output_info)
        log.set("finished and saved")
        try:
            write_to_drive()
        except:
            show_error('last error')
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
        show_error("authentification error")
        print("authentification error")
    try:
        fileDownloaded = drive.CreateFile({'id':'1zTuFXiai6eyDbejX1tyKt9B6phYUEj_C'})
        fileDownloaded.GetContentFile('data.csv')
    except:
        show_error("can't open the file")
        print("can't open the file")

    try:
        myCsvRow = str(time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(int(started)))) + ';' + str(time.strftime("%m-%d-%Y %H:%M:%S", time.localtime(int(ended)))) + ';'+ str(timedelta(seconds=round(elapsed,0))) + '\n'
        with open('data.csv','a') as fd:
            fd.write(myCsvRow)
        fileDownloaded.SetContentFile(f'data.csv')
        fileDownloaded.Upload()
        print('file uploaded successfully')
    except:
        show_error('error opening the file')
        print('error opening the file')
        quit()


app = tkinter.Tk()
app.geometry('180x240')

elapsed_time = tkinter.StringVar()
elapsed_time.set("00:00:00")

elapsed_label = tkinter.Label(app, textvariable=elapsed_time, fg="blue", font=("Arial Bold", 16))
elapsed_label.pack(side="bottom", ipady=10)

log = tkinter.StringVar()
log.set("start")

log_label = tkinter.Label(app, textvariable=log, fg="blue", font=("Arial Bold", 16))
log_label.pack(side="bottom", ipady=10)




starter = tkinter.Button(app, text="start", command= start_clicked)
starter.pack(side="top", ipady=10, ipadx=10, fill="x")


stop = tkinter.Button(app, text="stop and sync", command= stop_clicked)
stop.pack(side="top", ipady=10, ipadx=10, fill="x")

app.mainloop()