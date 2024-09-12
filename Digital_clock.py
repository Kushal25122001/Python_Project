from tkinter import *
import datetime


def date_time() :
    time = datetime.datetime.now()
    hr = time.strftime('%I')   # in I position hour will be return, strftime -> serftime
    mi = time.strftime('%M')   # in M position Min will be return
    sec = time.strftime('%S')   # in S position Sec will be return
    am = time.strftime('%p')    # in p position am/pm will be return

    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')


    # configeration of hr, min, sec, am
    lab_hr.config(text = hr)
    lab_min.config(text = mi)
    lab_sec.config(text = sec)
    lab_am.config(text = am)

    lab_date.config(text = date)
    lab_month.config(text = month)
    lab_year.config(text = year)
    lab_day.config(text = day)

    lab_hr.after(200, date_time)  # change after 200 milisecond



clock = Tk()
clock.title("Digital Clock")

clock.geometry("1000x500")

# bg color, font color etc can give using config func in background
clock.config(bg= "Blue")

#******************* Time ****************

# for hour
lab_hr = Label(clock, text="00", font=('Time New Roman', 60, "bold"), bg='red', fg="White")
lab_hr.place(x = 120, y = 50, height=110, width=100)

lab_hr_text = Label(clock, text="Hour", font=('Time New Roman', 25, "bold"), bg='red', fg="White")
lab_hr_text.place(x = 120, y = 190, height=40, width=100)

# for minutes
lab_min = Label(clock, text="00", font=('Time New Roman', 60, "bold"), bg='red', fg="White")
lab_min.place(x = 340, y = 50, height=110, width=100)

lab_min_text = Label(clock, text="Min", font=('Time New Roman', 25, "bold"), bg='red', fg="White")
lab_min_text.place(x = 340, y = 190, height=40, width=100)

# for second
lab_sec = Label(clock, text="00", font=('Time New Roman', 60, "bold"), bg='red', fg="White")
lab_sec.place(x = 560, y = 50, height=110, width=100)

lab_sec_text = Label(clock, text="Sec", font=('Time New Roman', 25, "bold"), bg='red', fg="White")
lab_sec_text.place(x = 560, y = 190, height=40, width=100)

# for AM/PM
lab_am = Label(clock, text="00", font=('Time New Roman', 60, "bold"), bg='red', fg="White")
lab_am.place(x = 780, y = 50, height=110, width=100)

lab_am_text = Label(clock, text="AM/PM", font=('Time New Roman', 25, "bold"), bg='red', fg="White")
lab_am_text.place(x = 780, y = 190, height=40, width=100)


#******************* Date ****************
# For date
lab_date = Label(clock, text="00", font=('Time New Roman', 60, "bold"), bg='red', fg="White")
lab_date.place(x = 120, y = 270, height=110, width=100)

lab_date_text = Label(clock, text="Date", font=('Time New Roman', 25, "bold"), bg='red', fg="White")
lab_date_text.place(x = 120, y = 410, height=40, width=100)

# For month
lab_month = Label(clock, text="00", font=('Time New Roman', 60, "bold"), bg='red', fg="White")
lab_month.place(x = 340, y = 270, height=110, width=100)

lab_month_text = Label(clock, text="Month", font=('Time New Roman', 25, "bold"), bg='red', fg="White")
lab_month_text.place(x = 340, y = 410, height=40, width=100)

# for year
lab_year = Label(clock, text="00", font=('Time New Roman', 60, "bold"), bg='red', fg="White")
lab_year.place(x = 560, y = 270, height=110, width=100)

lab_year_text = Label(clock, text="Year", font=('Time New Roman', 25, "bold"), bg='red', fg="White")
lab_year_text.place(x = 560, y = 410, height=40, width=100)

# for day
lab_day = Label(clock, text="00", font=('Time New Roman', 55, "bold"), bg='red', fg="White")
lab_day.place(x = 780, y = 270, height=110, width=100)

lab_day_text = Label(clock, text="Day", font=('Time New Roman', 25, "bold"), bg='red', fg="White")
lab_day_text.place(x = 780, y = 410, height=40, width=100)



date_time()


# To open the graphics
clock.mainloop()