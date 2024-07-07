from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # Title label

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Hospital Management System", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ============================== DataFrame ==============================================
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("arial", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=10, font=("arial", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=990, y=5, width=500, height=350)

        # ============================== BUTTONS ==============================================
        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=530, width=1530, height=60)

        # =============================== DataFrameLeft ===============================================
        # Variables
        self.NameTablet = StringVar()
        self.ReferenceNo = StringVar()
        self.Dose = StringVar()
        self.NoOfTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInfo = StringVar()
        self.BloodPressure = StringVar()
        self.PatientName = StringVar()
        self.PatientAddress = StringVar()

        # Name of Tablet
        lblNameTablet = Label(DataFrameLeft, text="Name OF Tablet", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        coNameTablet=tkk.Combobox(DataFrameLeextvariable=(self.NoOfTablets,state="randomly",
                                  font="arial",12,"bold"),width=33)
        
        comNameTablet = ttk.Combobox(DataFrameLeft, textvariable=self.NameTablet, font=("times new roman", 12, "bold"), width=33, state="readonly")
        comNameTablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNameTablet.grid(row=0, column=1)

        # Reference No
        lblref = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.ReferenceNo)
        txtref.grid(row=1, column=1)

        # Dose
        lblDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Dose)
        txtDose.grid(row=2, column=1)

        # No of Tablets
        lblNoOfTablets = Label(DataFrameLeft, font=("arial", 12, "bold"), text="No of Tablets:", padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.NoOfTablets)
        txtNoOfTablets.grid(row=3, column=1)

        # Lot
        lblLot = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.Lot)
        txtLot.grid(row=4, column=1)

        # Issue Date
        lblIssueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.IssueDate)
        txtIssueDate.grid(row=5, column=1)

        # Exp Date
        lblExpDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.ExpDate)
        txtExpDate.grid(row=6, column=1)

        # Daily Dose
        lblDailyDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.DailyDose)
        txtDailyDose.grid(row=7, column=1)

        # Side Effect
        lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.SideEffect)
        txtSideEffect.grid(row=8, column=1)

        # Further Info
        lblFurtherInfo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Further Info:", padx=2, pady=6)
        lblFurtherInfo.grid(row=9, column=0, sticky=W)
        txtFurtherInfo = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.FurtherInfo)
        txtFurtherInfo.grid(row=9, column=1)

        # Blood Pressure
        lblBloodpressure = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBloodpressure.grid(row=10, column=0, sticky=W)
        txtBloodpressure = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.BloodPressure)
        txtBloodpressure.grid(row=10, column=1)

        # Patient Name
        lblPatientName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblPatientName.grid(row=11, column=0, sticky=W)
        txtPatientName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.PatientName)
        txtPatientName.grid(row=11, column=1)

        # Patient Address
        lblPatientAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lblPatientAddress.grid(row=12, column=0, sticky=W)
        txtPatientAddress = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35, textvariable=self.PatientAddress)
        txtPatientAddress.grid(row=12, column=1)


    #   ==================================================== Buttons ====================================================

    btnPrescription=Button(Buttonframe,text="Presciption",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
    btnPrescription.grid(row=0,column=0)

    btnPrescription=Button(Buttonframe,text="Presciption",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
    btnPrescription.grid(row=0,column=1)

    btnUpdate=Button(Buttonframe,text="Update",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
    btnUpdate.grid(row=0,column=2)

    btnDelete=Button(Buttonframe,text="Delete",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
    btnDelete.grid(row=0,column=3)
    
    btnClear=Button(Buttonframe,text="Clear",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
    btnClear.grid(row=0,column=4)

    btnExist=Button(Buttonframe,text="Exist",font=("arial",12,"bold"),width=23,height=16,padx=2,pady=6)
    btnExist.grid(row=0,column=5)

    # ================================================= Table =========================================================
    # ================================================= Scrollbar =====================================================

    scroll_x=ttk.Scrollbar(DetailsFrame orient=HORIZONTAL)
    scroll_x=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
    self.hospital_tablets=ttk.Treeview(FrameDetails,column=('nameoftable',"ref","dose","nooftablets","lot","issuedaate",
                "expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,,yscrollcommand_y.set)

    scroll_x.pack=(side=BOTTON,fill=x)
    scroll_y.pack=(side=RIGHT,fill=y)

    scroll_x=ttk Scrollbar(command=self.hosptial_table.xview)
    scroll_y=ttk Scrollbar(command=self.hosptial_table.yview)

    self.hosptial_table.heading("nameoftable",text="Name of Table")
    self.hosptial_table.heading("ref",text="Reference No")
    self.hosptial_table.heading("dose",text="Dose")
    self.hosptial_table.heading("mooftablets",text="No of tablets")
    self.hospital_table.heading("lot",text="Lot")
    self.hosptial_table.heading("issuedate",text="Issue Date")
    self.hosptial_table.heading("expdate",text="Exp Date")
    self.hosptial_table.heading("dailydose",text="Daily DOse")
    self.hosptial_table.heading("storage",text="storage")
    self.hosptial_table.heading("nhsnumber",text="NHS Number")
    self.hosptial_table.heading("pname",text="Patient name")
    self.hosptial_table.heading("dob",text="DOB")
    self.hosptial_table.heading("address",text="Address")

    self.hosptial_table["show"]="headings"

    self.hospital_table.pack(fill=BOTH,expand=1)

    self.hosptial_tablecolumn("nameoftable")



    # ======================================= Functionality Decleartion ==========================================

    def iPresciptionData(self):
        if self.NameofTablets.get()=='' or self.ref.get()=""
        messagebox.showerror("Error","All fields are required")     
        elif:
            conn=mysql.connector(host="localhost",username="root",password="Test123",database="Myadata")
            my_cursor=conn.Cursor()
            my_cursor.execcute("insert into hosptial.values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s),("
                               
                                self.NameTablet,
                                self.ReferenceNo
                                self.Dose
                                self.NoOfTablets
                                self.Lot 
                                self.IssueDate
                                self.ExpDate
                                self.DailyDose
                                self.SideEffect
                                self.FurtherInfo
                                self.BloodPressure
                                self.PatientName
                                self.PatientAddress
                               
                               )
    

if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()
