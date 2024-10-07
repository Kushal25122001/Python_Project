from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox
import tkinter
import datetime

class LibraryManageSystem :
    def __init__(self, root) :
        self.root = root
        self.root.title("Library management System")
        self.root.geometry("1550x800+0+0")


        ################ Variable #######################
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.auther_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()


        # for title block
        lbltitle = Label(self.root, text ="LIBRARY MANAGEMENT SYSTEM", bg = "powder blue", fg = "green", bd = 20, relief = RIDGE, font = ("times new roman", 50, "bold"), padx = 2, pady = 6 )
        lbltitle.pack(side = TOP, fill = X)

        # for next frame1(after title block)
        frame = Frame(self.root, bd = 12, relief=RIDGE, padx =20 , bg = "powder blue")
        frame.place(x = 0, y = 130, width = 1530, height= 400)

        ####################### Data Frame Left ##################
        DataFrameLeft = LabelFrame(frame, text ="Library Membership Information", bg = "powder blue", fg = "green", bd = 12, relief = RIDGE, font = ("times new roman", 15, "bold"))
        DataFrameLeft.place(x = 0, y = 5, width = 860, height = 350)

        lblMember = Label(DataFrameLeft,bg = "powder blue", text ="Member Type", font = ("times new roman", 15, "bold"), padx = 2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        # lblMember combo box
        comMember = ttk.Combobox(DataFrameLeft, font = ("arial", 12, "bold"),textvariable=self.member_var, width=31, state="readonly")
        comMember["value"] = ("Admin staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0 , column=1)

        # lable and entry box for PNR_No
        lblPRN_No = Label(DataFrameLeft,bg = "powder blue", text ="PRN No", font = ("arial", 12, "bold"), padx = 2)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.prn_var, width=29)
        txtPRN_No.grid(row=1, column=1)

        # lable and entry box for ID No
        lblID_No = Label(DataFrameLeft,bg = "powder blue", text ="ID No", font = ("arial", 12, "bold"), padx = 2, pady=4)
        lblID_No.grid(row=2, column=0, sticky=W)
        txtID_No = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.id_var, width=29)
        txtID_No.grid(row=2, column=1)

        # lable and entry box for First name
        lblFirstName = Label(DataFrameLeft,bg = "powder blue", text ="First Name", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.firstname_var, width=29)
        txtFirstName.grid(row=3, column=1)

        # lable and entry box for Last name
        lblLastName = Label(DataFrameLeft,bg = "powder blue", text ="Last Name", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.lastname_var, width=29)
        txtLastName.grid(row=4, column=1)

        # lable and entry box for Address1
        lblAddress1 = Label(DataFrameLeft,bg = "powder blue", text ="Address1", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.address1_var, width=29)
        txtAddress1.grid(row=5, column=1)

        # lable and entry box for Address2
        lblLastName = Label(DataFrameLeft,bg = "powder blue", text ="Address2", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblLastName.grid(row=6, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.address2_var, width=29)
        txtLastName.grid(row=6, column=1)

        # lable and entry box for Postal Code
        lblPostCode = Label(DataFrameLeft,bg = "powder blue", text ="Post Code", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.postcode_var, width=29)
        txtPostCode.grid(row=7, column=1)

        # lable and entry box for mobile
        lblMobile = Label(DataFrameLeft,bg = "powder blue", text ="Mobile", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8, column=1)

        # lable and entry box Book ID
        lblBookID = Label(DataFrameLeft,bg = "powder blue", text ="Book ID", font = ("arial", 12, "bold"), padx = 2)
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID = Entry(DataFrameLeft, font = ("arial", 12, "bold"), textvariable=self.bookid_var, width=33)
        txtBookID.grid(row=0, column=3)

        # lable and entry box for Book Title
        lblBookTitle = Label(DataFrameLeft,bg = "powder blue", text ="Book Title", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.booktitle_var, width=29)
        txtBookTitle.grid(row=1, column=3)

        # lable and entry box for Author
        lblAuthor = Label(DataFrameLeft,bg = "powder blue", text ="Author", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.auther_var, width=29)
        txtAuthor.grid(row=2, column=3)

        # lable and entry box for Date Borrowed
        lblDateBorrowed = Label(DataFrameLeft,bg = "powder blue", text ="Date Borrowed", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.dateborrowed_var, width=29)
        txtDateBorrowed.grid(row=3, column=3)

        # lable and entry box for Date Due
        lblDateDue = Label(DataFrameLeft,bg = "powder blue", text ="Date Due", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.datedue_var, width=29)
        txtDateDue.grid(row=4, column=3)

        # lable and entry box for Days on Book
        lblDaysonBook = Label(DataFrameLeft,bg = "powder blue", text ="Days on Book", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblDaysonBook.grid(row=5, column=2, sticky=W)
        txtDaysonBook= Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.daysonbook_var, width=29)
        txtDaysonBook.grid(row=5, column=3)

        # lable and entry box for Late return fine
        lblLateReturnFine = Label(DataFrameLeft,bg = "powder blue", text ="Late Return Fine", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine= Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.lateratefine_var, width=29)
        txtLateReturnFine.grid(row=6, column=3)

        # lable and entry box for Over date
        lblOverdate = Label(DataFrameLeft,bg = "powder blue", text ="Over Date", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblOverdate.grid(row=7, column=2, sticky=W)
        txtOverdate= Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.dateoverdue_var, width=29)
        txtOverdate.grid(row=7, column=3)

        # lable and entry box for Actual price
        lblActualPrice = Label(DataFrameLeft,bg = "powder blue", text ="Actual Price", font = ("arial", 12, "bold"), padx = 2, pady=6)
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice= Entry(DataFrameLeft, font = ("arial", 13, "bold"), textvariable=self.finalprice_var, width=29)
        txtActualPrice.grid(row=8, column=3)

        ####################### Data Frame Right ##################
        DataFrameRight = LabelFrame(frame, text ="Book Details", bg = "powder blue", fg = "green", bd = 12,padx = 20, relief = RIDGE, font = ("arial", 12, "bold"))
        DataFrameRight.place(x = 870, y = 5, width = 580, height = 350)

        # for text box in the data frame right
        self.txtBox = Text(DataFrameRight, font = ("arial", 12, "bold"), width = 32, height = 22, padx = 2, pady = 6)
        self.txtBox.grid(row = 0, column = 2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row = 0, column = 1, sticky="ns")

        # list box inside the text box in the dataframe right
        listBooks = ['Python Crash Course', 'Automate the Boring Stuff with Python', 'Learning Python',
                        'Python Cookbook', 'Fluent Python', 'Effective Python', 'Python Data Science Handbook',
                        'Head First Programming', 'Python for Data Analysis', 'Django for Beginners', 'Python Tricks',
                        'Introduction to Machine Learning with Python', 'Python Programming', 'Mastering Python Design Patterns',
                        'Test-Driven Development with Python', 'Python Testing with pytest',
                        'Data Science from Scratch', 'Python for Everybody', 'Python Machine Learning', 'Deep Learning with Python',
                        'Machine Learning', 'Deep Learning', 'Flask']
        

        def SelectBook(event=None) :
            value = str(listBox.get(listBox.curselection()))
            x = value
            if (x == "Python Crash Course"):
                self.bookid_var.set("BKID1")
                self.booktitle_var.set("Python course")
                self.auther_var.set("poul Barry")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.788")

            elif (x == "Automate the Boring Stuff with Python"):
                self.bookid_var.set("BKID2")
                self.booktitle_var.set("Python course stuff")
                self.auther_var.set("Barry")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.308")

            elif (x == "Learning Python"):
                self.bookid_var.set("BKID3")
                self.booktitle_var.set("Learning Python")
                self.auther_var.set("kushal sam")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.800")

            elif (x == "Python Cookbook"):
                self.bookid_var.set("BKID4")
                self.booktitle_var.set("Python Cookbook")
                self.auther_var.set("Shyam")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.700")

            elif (x == "Fluent Python"):
                self.bookid_var.set("BKID5")
                self.booktitle_var.set("Fluent Python")
                self.auther_var.set("poul Barry")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.80")


        listBox = Listbox(DataFrameRight, font = ("arial", 12, "bold"), width = 20, height = 21)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row = 0, column =0, padx = 4)
        listScrollbar.config(command= listBox.yview)
        

        for item in listBooks :
            listBox.insert(END, item)



        ##############################  Buttons Frame ##################
        Framebutton = Frame(self.root, bd = 12, relief=RIDGE, padx =20 , bg = "powder blue")
        Framebutton.place(x = 0, y = 530, width = 1530, height= 70)

        # button for add data
        btnADDData = Button(Framebutton, command= self.add_data, text = "Add Data", font = ("arial", 12, "bold"), width = 30,fg="blue")
        btnADDData.grid(row = 0, column=0)

        # button for show data
        btnShowdata = Button(Framebutton,command=self.show_data, text = "Show Data", font = ("arial", 12, "bold"), width = 30,fg="blue")
        btnShowdata.grid(row = 0, column=1)

        # button for update
        btnUpdate = Button(Framebutton, command= self.update, text = "Update", font = ("arial", 12, "bold"), width = 30,fg="blue")
        btnUpdate.grid(row = 0, column=2)

        # button for delete
        btnDelete = Button(Framebutton, command=self.delete, text = "Delete", font = ("arial", 12, "bold"), width = 30,fg="blue")
        btnDelete.grid(row = 0, column=3)

        # button for reset
        btnReset = Button(Framebutton,command=self.reset, text = "Reset", font = ("arial", 12, "bold"), width = 30,fg="blue")
        btnReset.grid(row = 0, column=4)

        # button for exit
        btnExit = Button(Framebutton, command=self.iexit, text = "Exit", font = ("arial", 12, "bold"), width = 23,fg="blue")
        btnExit.grid(row = 0, column=5)

        

        ##############################  Information Frame ##################
        FrameDetails = Frame(self.root, bd = 12, relief=RIDGE, padx =20 , bg = "powder blue")
        FrameDetails.place(x = 0, y = 590, width = 1530, height= 210)

        # Table frame inside frame details to showing the database data
        Table_frame =  Frame(FrameDetails,bd = 6, relief=RIDGE, bg = "powder blue")
        Table_frame.place(x = 0, y = 2, width = 1460, height= 190)

        xscroll = ttk.Scrollbar(Table_frame, orient = HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient = VERTICAL)

        # devide the frame into grid based column / writing dummy data for tree view
        self.library_table = ttk.Treeview(Table_frame, column = ("membertype", "prnno", "title", "firstname", "lastname",
                                                                    "address1", "address2", "postid", "mobile", "bookid",
                                                                    "booktitle", "author", "dateborrowed", "datedue", "days",
                                                                    "latereturnfine", "dateoverdue", "finalprice"),
                                                                    xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        
        xscroll.pack(side = BOTTOM, fill= X)
        yscroll.pack(side = RIGHT, fill= Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype", text = "Member Type")
        self.library_table.heading("prnno", text = "PRN No")
        self.library_table.heading("title", text = "Title")
        self.library_table.heading("firstname", text = "First name")
        self.library_table.heading("lastname", text = "Last name")
        self.library_table.heading("address1", text = "Address1")
        self.library_table.heading("address2", text = "Address2")
        self.library_table.heading("postid", text = "Post ID")
        self.library_table.heading("mobile", text = "Mobile No")
        self.library_table.heading("bookid", text = "Book ID")
        self.library_table.heading("booktitle", text = "Book Title")
        self.library_table.heading("author", text = "Author")
        self.library_table.heading("dateborrowed", text = "Date of Borrowed")
        self.library_table.heading("datedue", text = "Date Due")
        self.library_table.heading("days", text = "Days on Book")
        self.library_table.heading("latereturnfine", text = "Late Return Fine")
        self.library_table.heading("dateoverdue", text = "Date Over Due")
        self.library_table.heading("finalprice", text = "Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill = BOTH, expand=1)

        ## to reduce the database column width
        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fatch_data()

        ## Bind for the table to fetch the info automatically to all text field from the database 
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    ## to store the data in database and show into the database frame
    def add_data(self):
        conn = sql.connect(host = "localhost", username ="root", password = "Kush@l2018", database = "library_management")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                                                        self.member_var.get(),
                                                                                                                                        self.prn_var.get(),
                                                                                                                                        self.id_var.get(),
                                                                                                                                        self.firstname_var.get(),
                                                                                                                                        self.lastname_var.get(),
                                                                                                                                        self.address1_var.get(),
                                                                                                                                        self.address2_var.get(),
                                                                                                                                        self.postcode_var.get(),
                                                                                                                                        self.mobile_var.get(),
                                                                                                                                        self.bookid_var.get(),
                                                                                                                                        self.booktitle_var.get(),
                                                                                                                                        self.auther_var.get(),
                                                                                                                                        self.dateborrowed_var.get(),
                                                                                                                                        self.datedue_var.get(),
                                                                                                                                        self.daysonbook_var.get(),
                                                                                                                                        self.lateratefine_var.get(),
                                                                                                                                        self.dateoverdue_var.get(),
                                                                                                                                        self.finalprice_var.get()
                                                                                                                                        
                                                                                                                                    ))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success", "Member has been inserted successfully")

    ## To fetch the data into the data frame
    def fatch_data(self) :
        conn = sql.connect(host = "localhost", username ="root", password = "Kush@l2018", database = "library_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0 :
            self.library_table.delete(*self.library_table.get_children())
            for i in rows :
                self.library_table.insert("", END, values = i)
            conn.commit()
        conn.close()
    
    ## To show the data in the text field if we click a row from the database frame
    def get_cursor(self, event = None) :
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])
        self.auther_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook_var.set(row[14])
        self.lateratefine_var.set(row[15])
        self.dateoverdue_var.set(row[16])
        self.finalprice_var.set(row[17])

    def show_data(self) :
        self.txtBox.insert(END, "Member Type :\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No :\t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No :\t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "First Name :\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "Lastname :\t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1 :\t\t" + self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2 :\t\t" + self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Post Code :\t\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No :\t\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID :\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title :\t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Auther :\t\t" + self.auther_var.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed :\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date Due:\t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "Days On Book :\t\t" + self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "Late Rate Fine :\t\t" + self.lateratefine_var.get() + "\n")
        self.txtBox.insert(END, "Date Overdue :\t\t" + self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END, "Final Price :\t\t" + self.finalprice_var.get() + "\n")


    def reset(self) :
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.lateratefine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")
        self.txtBox.delete("1.0", END)

    def iexit(self) :
        iexit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit")
        if iexit > 0 :
            self.root.destroy()
            return
    
    def update(self) :
        conn = sql.connect(host = "localhost", username ="root", password = "Kush@l2018", database = "library_management")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, Postid=%s, Mobile=%s, Bookid=%s, librarycol=%s, Auther=%s, Dateborrowed=%s, Datedue=%s, Daysofbook=%s, Latereturnfine=%s, Dateoverdue=%s, Finalprice=%s where PRN_NO=%s and ID=%s",(
                                                                                                                                                                                                                                                self.member_var.get(),
                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                self.firstname_var.get(),
                                                                                                                                                                                                                                                self.lastname_var.get(),
                                                                                                                                                                                                                                                self.address1_var.get(),
                                                                                                                                                                                                                                                self.address2_var.get(),
                                                                                                                                                                                                                                                self.postcode_var.get(),
                                                                                                                                                                                                                                                self.mobile_var.get(),
                                                                                                                                                                                                                                                self.bookid_var.get(),
                                                                                                                                                                                                                                                self.booktitle_var.get(),
                                                                                                                                                                                                                                                self.auther_var.get(),
                                                                                                                                                                                                                                                self.dateborrowed_var.get(),
                                                                                                                                                                                                                                                self.datedue_var.get(),
                                                                                                                                                                                                                                                self.daysonbook_var.get(),
                                                                                                                                                                                                                                                self.lateratefine_var.get(),
                                                                                                                                                                                                                                                self.dateoverdue_var.get(),
                                                                                                                                                                                                                                                self.finalprice_var.get(),
                                                                                                                                                                                                                                                self.prn_var.get(),
                                                                                                                                                                                                                                                self.id_var.get()

                                                                                                                                                                                                                                                ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "member has been updated")

    def delete(self) :
        if (self.prn_var.get() == "") or (self.id_var.get() == "") :
            messagebox.showerror("error", "First select the member")
        else :
            conn = sql.connect(host = "localhost", username ="root", password = "Kush@l2018", database = "library_management")
            my_cursor = conn.cursor()
            query = "delete from library where PRN_NO=%s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query, value)

            conn.commit()
            self.fatch_data()
            conn.close()
            self.reset()

            messagebox.showinfo("Success", "Member has been deleted")



if __name__ == "__main__":
    root = Tk()

    obj = LibraryManageSystem(root)
    root.mainloop()