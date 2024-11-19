from tkinter import *
from tkinter import ttk  # Import ttk for Combobox

# import mysql.connector
class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        # Title Label
        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM",
                         bg="powder blue", fg="green", bd=20, relief=RIDGE,
                         font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        # Main Frame
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # Left Frame
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information",
                                   bg="powder blue", fg="green", bd=20, relief=RIDGE,
                                   font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        # Member Type
        lb1Member = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Member Type", padx=2, pady=6,
                          bg="powder blue")
        lb1Member.grid(row=0, column=0, sticky=W)
        comMember = ttk.Combobox(DataFrameLeft, state="readonly", font=("arial", 12, "bold"),
                                 width=27)
        comMember['values'] = ("Admin Staff", "Lecturer", "Student")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        # PRN No.
        lb1PRN_NO = Label(DataFrameLeft, font=("arial", 12, "bold"), text="PRN No: ", padx=2, bg="powder blue")
        lb1PRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtPRN_NO.grid(row=1, column=1)

        # ID No.
        lblTitle = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ID No: ", padx=2, pady=4, bg="powder blue")
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtTitle.grid(row=2, column=1)

        # First Name
        lblFirstName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="First Name", padx=2, pady=6,
                             bg="powder blue")
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtFirstName.grid(row=3, column=1)

        # Last Name
        lblLastName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Last Name", padx=2, pady=6,
                            bg="powder blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtLastName.grid(row=4, column=1)

        # Address 1
        lblAddress1 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address 1", padx=2, pady=6,
                            bg="powder blue")
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtAddress1.grid(row=5, column=1)

        # Address 2
        lblAddress2 = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Address 2", padx=2, pady=6,
                            bg="powder blue")
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtAddress2.grid(row=6, column=1)

        # Post Code
        lblPostCode = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Post Code", padx=2, pady=4,
                            bg="powder blue")
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtPostCode.grid(row=7, column=1)

        # Mobile
        lblMobile = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Mobile", padx=2, pady=6,
                          bg="powder blue")
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Book Id:", padx = 2, bg = "powder blue")
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font = ("arial", 12, "bold"), width = 29)
        txtBookId.grid(row=0, column=3)
        lblBookTitle = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Book Title:", padx = 2, pady = 6, bg = "powder blue")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font = ("arial", 12, "bold"), width = 29)
        txtBookTitle.grid(row=1, column=3)
        lblAuther=Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Auther Name:", padx = 2, pady = 6, bg = "powder blue")
        lblAuther.grid(row=2, column=2, sticky=W)
        txtAuther = Entry(DataFrameLeft, font = ("arial", 12, "bold"), width = 29)
        txtAuther.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Date Borrowed: ", padx = 2, pady = 6, bg = "powder blue")
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font = ("arial", 12, "bold"), width = 29)
        txtDateBorrowed.grid(row=3, column=3, sticky=W)
        lblDateDue = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Date Due:", padx = 2, pady = 6, bg = "powder blue")
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font = ("arial", 12, "bold"), width = 29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Days On Book: ", padx = 2, pady = 6, bg = "powder blue")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial", 12, "bold"), width=29)
        txtDaysOnBook.grid(row=5, column=3)


        lblLateReturnFine = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Late Return Fine: ", padx = 2, pady = 6, bg = "powder blue")

        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font = ("arial", 12, "bold"), width = 29)
        txtLateReturnFine.grid(row=6, column=3)
        lblDateOverdate = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Date Over Due: ", padx = 2, pady = 6, bg = "powder blue")
        lblDateOverdate.grid(row=7, column=2, sticky=W)
        txtDateOverdate = Entry(DataFrameLeft, font = ("arial", 12, "bold"), width = 29)
        txtDateOverdate.grid(row=7, column=3)
        lblActualPrice = Label(DataFrameLeft, font = ("arial", 12, "bold"), text = "Actual Price:", padx = 2, pady = 6, bg = "powder blue")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font = ("arial", 12, "bold"), width = 29)
        txtActualPrice.grid(row=8, column=3)

        # Right Frame
        DataFrameRight = LabelFrame(frame, text="Book Info", bg="powder blue", fg="green", bd=20,
                                    relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=600, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listBoooks=["Head Firt Book','Learn Python The Hard Way','Python Programming", "Secrete Rahshy","Python CookBook",'Into to Machine Learning',"Fluent Pyt",
'Machine tecno','My Python', 'Joss Ellif guru','Elite Jungle python','Jungli Python','Mumbai Python','Pune Pytho',
'Machine python','Advance Python','Inton Python','RedChilli Python','Ishq Python']

        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=16)
        listBox.grid(row=0, column=0, padx=4)

        listScrollbar.config(command=listBox.yview)
        for item in listBoooks:
            listBox.insert(END, item)

        # Buttons Frame
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(Framebutton, text="Add Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)
        btnAddData = Button(Framebutton, text="Show Data", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=1)
        btnAddData = Button(Framebutton, text="Update", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=2)
        btnAddData = Button(Framebutton, text="Delete", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=3)
        btnAddData = Button(Framebutton, text="Reset", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=4)
        btnAddData = Button(Framebutton, text="Exit", font=("arial", 12, "bold"), width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=5)

        # Details Frame
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1530, height=195)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)
        self.library_table = ttk.Treeview(Table_frame,column=("memebertype", "prnno", "title", "firtname", "lastname", "adress1","adress2", "postid", "mobile", "bookid", "booktitle", "auther","dateborrowed","datedue", "days", "latereturnfine", "dateoverdue", "finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("memebertype", text="Member Type")
        self.library_table.heading("prnno", text="Reference No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firtname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("adress1", text="Address1")
        self.library_table.heading("adress2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("auther", text="Auther")
        self.library_table.heading("dateborrowed", text="Date Of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("latereturnfine", text="Late ReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue")
        self.library_table.heading("finalprice", text="Final Price")
        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("memebertype", width=100)

        self.library_table.column("prnno", width=100)

        self.library_table.column("title", width=100)

        self.library_table.column("firtname", width=108)

        self.library_table.column("lastname", width=100)
        self.library_table.column("adress1", width=100)

        self.library_table.column("adress2", width=100)
        self.library_table.column("postid", width=100)

        self.library_table.column("mobile", width=100)

        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)

        self.library_table.column("auther", width=100)

        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)

        self.library_table.column("days", width=100)

        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

root = Tk()
obj = LibraryManagementSystem(root)
root.mainloop()
