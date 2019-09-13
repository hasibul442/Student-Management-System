from tkinter import *
from tkinter import ttk,messagebox
import pymysql

class Student:
    def __init__(self, root):
        self.root=root
        self.root.title("Portal")
        self.root.geometry("1350x680+0+0")

        title = Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="green",fg="White")
        title.pack(side=TOP,fill=X)

        #---------------All Variables------------------
        
        self.rollno_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()


        #########_________________Footer Frame_________________###########
        
        Footer_Frame = Frame(self.root,bg="blue")
        Footer_Frame.place(x=0,y=650,width=1400,height=70)
       



        #########_________________Manage Frame_________________###########
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=0,y=83,width=380,height=570)

        m_title = Label(Manage_Frame,text="Manage Students",font=("times new roman",25,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=10)


                                        ####=============Label name==========
        lbl_roll = Label(Manage_Frame,text="Roll No.",font=("times new roman",20,"bold"),bg="crimson",fg="black")
        lbl_roll.grid(row=1,column=0,pady=10,padx=5,sticky="w")

        lbl_name= Label(Manage_Frame,text="Name",font=("times new roman",20,"bold"),bg="crimson",fg="black")
        lbl_name.grid(row=2,column=0,pady=10,padx=5,sticky="w")

        lbl_email = Label(Manage_Frame,text="Email",font=("times new roman",20,"bold"),bg="crimson",fg="black")
        lbl_email.grid(row=3,column=0,pady=10,padx=5,sticky="w")

        lbl_gender = Label(Manage_Frame,text="Gender",font=("times new roman",20,"bold"),bg="crimson",fg="black")
        lbl_gender.grid(row=4,column=0,pady=10,padx=5,sticky="w")

        lbl_contact = Label(Manage_Frame,text="Contact",font=("times new roman",20,"bold"),bg="crimson",fg="black")
        lbl_contact.grid(row=5,column=0,pady=10,padx=5,sticky="w")

        lbl_dateofbirth = Label(Manage_Frame,text="D.O.B",font=("times new roman",20,"bold"),bg="crimson",fg="black")
        lbl_dateofbirth.grid(row=6,column=0,pady=10,padx=5,sticky="w")

        lbl_address = Label(Manage_Frame,text="Address",font=("times new roman",20,"bold"),bg="crimson",fg="black")
        lbl_address.grid(row=7,column=0,pady=10,padx=5,sticky="w")


                                         ####=============Text Box name==========
        txt_roll=Entry(Manage_Frame,font=("time new roman",15,"normal"),textvariable=self.rollno_var)
        txt_roll.grid(row=1,column=1,pady=10,padx=5,sticky="w")

        txt_name=Entry(Manage_Frame,font=("time new roman",15,"normal"),textvariable=self.name_var)
        txt_name.grid(row=2,column=1,pady=10,padx=5)

        txt_email=Entry(Manage_Frame,font=("time new roman",15,"normal"),textvariable=self.email_var)
        txt_email.grid(row=3,column=1,pady=10,padx=5)

        combo_gender=ttk.Combobox(Manage_Frame,font=("time new roman",15,"normal"),state="readonly",textvariable=self.gender_var)
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=5)

        txt_contact=Entry(Manage_Frame,font=("time new roman",15,"normal"),textvariable=self.contact_var)
        txt_contact.grid(row=5,column=1,pady=10,padx=5)

        txt_dateofbath=Entry(Manage_Frame,font=("time new roman",15,"normal"),textvariable=self.dob_var)
        txt_dateofbath.grid(row=6,column=1,pady=10,padx=5)

        self.txt_address=Text(Manage_Frame,width=20,height=3,font=("",15,))
        self.txt_address.grid(row=7,column=1,pady=10,padx=5)

        #####_____________________Button Frame__________________
        btn_frame=Frame(Manage_Frame,bd=1,relief=RIDGE,bg="crimson")
        btn_frame.place(x=0,y=500,width=372,height=50)

        #########_______________Button___________________
        addbtn=Button(btn_frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=3,pady=10)
        updatebtn=Button(btn_frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=8,pady=10)
        deletebtn=Button(btn_frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=8,pady=10)
        clearbtn=Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=8,pady=10)



        #########_________________Details Frame_________________###########
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Detail_Frame.place(x=380,y=83,width=1000,height=570)

        lbl_search=Label(Detail_Frame,text="Search By",bg="black",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,padx=20,pady=10)

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=15,font=("time new roman",13,"normal"),state="readonly")
        combo_search['values']=("Roll","Name","Contact")
        combo_search.grid(row=0,column=1,pady=20,padx=10)

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,font=("time new roman",14,"normal"))
        txt_search.grid(row=0,column=2,pady=10,padx=20)

        searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=20,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=20,pady=10)

        ##########_________table Frame____________________

        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="black")
        Table_Frame.place(x=10,y=70,width=950,height=480)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll",text="Roll NO.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contacr")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("address",text="Address")
        self.student_table['show']='headings'

        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=150)
        self.student_table.column("email",width=150)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=140)
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=200)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_data)
        self.fetch_data()

    def add_students(self):

        if self.rollno_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are required!!!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="studentdata")
            cur=con.cursor()
            cur.execute("insert into student_info values(%s,%s,%s,%s,%s,%s,%s)",(self.rollno_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_address.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record Has Been Added")


    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="studentdata")
        cur=con.cursor()
        cur.execute("select * from student_info ")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    
    def clear(self):
        self.rollno_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_data(self,ev):
        curosor_row=self.student_table.focus()
        contents=self.student_table.item(curosor_row)
        row=contents['values']

        self.rollno_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])


    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="studentdata")
        cur=con.cursor()
        cur.execute("update student_info set name=%s,email=%s,gender=%s,contact=%s,DOB=%s,address=%s where roll=%s",(
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_address.get('1.0',END),
                                                                            self.rollno_var.get()
                                                                            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="studentdata")
        cur=con.cursor()  
        cur.execute("delete from student_info where roll=%s",self.rollno_var.get())     
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="studentdata")
        cur=con.cursor()
        cur.execute("select * from student_info where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()


root=Tk()
ob=Student(root)
root.mainloop()