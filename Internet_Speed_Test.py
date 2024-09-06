from tkinter import *
import speedtest

def speedCheck() :
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3)) + " Mbps"
    up =  str(round(sp.upload()/(10**6), 3)) + " Mbps"
    lab_down.config(text = down)
    lab_up.config(text = up)


# Calling tkinter class
sp = Tk()

sp.title("Internet Speed Test")
# window size
sp.geometry("500x650")
# bg color, font color etc can give using config func
sp.config(bg= "Blue")

# Putting label
lab = Label(sp, text = "Internet Speed Test", font = ("Time New Roman", 40, "bold"), bg = "Blue", fg = "White")
# Place the label
lab.place(x = 60, y = 40, height = 50,width = 380)

# Label for download speed
lab = Label(sp, text = "Download Speed", font = ("Time New Roman", 40, "bold"))
lab.place(x = 60, y = 130, height = 50, width = 380)

lab_down = Label(sp, text = "00 ", font = ("Time New Roman", 40, "bold"))
lab_down.place(x = 60, y = 200, height = 50, width = 380)

# Label for upload speed
lab = Label(sp, text = "Upload Speed", font = ("Time New Roman", 40, "bold"))
lab.place(x = 60, y = 290, height = 50, width = 380)

lab_up= Label(sp, text = "00", font = ("Time New Roman", 40, "bold"))
lab_up.place(x = 60, y = 360, height = 50, width = 380)

button = Button(sp, text = "Check Speed", font = ("Time New Roman", 40, "bold"), relief = RAISED, bg = "Red", command = speedCheck)
button.place(x = 60, y = 460, height = 50, width = 380)


# To open a window
sp.mainloop()