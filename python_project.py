from tkinter import *


class Bill_App:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1500x780+0+0")
        self.window.title("BILLING SOFTWARE")
        # self.window.iconbitmap('coffee.icon')
        bg_colour="#5D6D7E"

        # ---------------Top Label---------------
        Label(self.window, text="BILLING   SOFTWARE", bd=12, fg="#FBFCFC", bg=bg_colour, relief=GROOVE, font=("times new roman", 30, "bold")).pack(pady=18, fill=X)

        # ---------------Customer details widget---------------
        f1 = LabelFrame(self.window, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 20, "bold"), bg=bg_colour, fg="#3498DB", pady=10)
        f1.place(x=0, y=91, relwidth=1)

        cname_lbl = Label(f1, text="Customer Name", bg=bg_colour, fg="#FBFCFC",font=("times new roman",15,"bold")).grid(row=0, column=0, padx=10, pady=5)
        cname_input = Entry(f1, font=("arial", 10), bd=4, relief=SUNKEN, width=50).grid(row=0, column=1, padx=50)

        contact_lbl = Label(f1, text="Contact Number", bg=bg_colour, fg="#FBFCFC",font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=50, pady=5)
        contact_input = Entry(f1, font=("arial", 10), bd=4, relief=SUNKEN, width=50).grid(row=0, column=3)

        # ---------------Coffee Frame widget---------------
        f2 = LabelFrame(self.window, text="Coffee", bd=10, relief=GROOVE,font=("times new roman", 18, "bold"), bg=bg_colour, fg="#3498DB")
        f2.place(x=0, y=190, relwidth=0.3, height=500)

        cofee_item01 = Label(f2, text="Coffee", font=("arial",15), bg=bg_colour, fg="#FBFCFC").grid(row=0, column=0,padx=10, pady=30)
        coffee_item01_input = Entry(f2, font=("arial",15), bd=5, width=10).grid(row=0, column=1, padx=4)

        cofee_item02 = Label(f2, text="Cold Cofee", font=("arial", 15), bg=bg_colour, fg="#FBFCFC").grid(row=1, column=0,padx=10, pady=30)
        coffee_item02_input = Entry(f2, font=("arial", 15), bd=5, width=10).grid(row=1, column=1, padx=4)

        cofee_item03 = Label(f2, text="Cold Cream Coffee ", font=("arial", 15), bg=bg_colour, fg="#FBFCFC").grid(row=2, column=0,padx=10, pady=30)
        coffee_item03_input = Entry(f2, font=("arial", 15), bd=5, width=10).grid(row=2, column=1, padx=4)

        cofee_item04 = Label(f2, text="Hot Cream Coffee", font=("arial", 15), bg=bg_colour, fg="#FBFCFC").grid(row=3, column=0,padx=10, pady=30)
        coffee_item04_input = Entry(f2, font=("arial", 15), bd=5, width=10).grid(row=3, column=1, padx=4)

        cofee_item05 = Label(f2, text="Black Coffee", font=("arial", 15), bg=bg_colour, fg="#FBFCFC").grid(row=4, column=0,padx=10, pady=30)
        coffee_item05_input = Entry(f2, font=("arial", 15), bd=5, width=10).grid(row=4, column=1, padx=4)
        
        # ---------------Tea Frame widget---------------
        # f3 = LabelFrame(self.window, text="Tea", bd=10, relief=GROOVE, font=("times new roman", 18, "bold"),bg=bg_colour, fg="#3498DB", padx=20)
        # f3.place(x=455, y=190, relwidth=0.3, height=500)

        # tea_item01 = Label(f3, text="Tea", font=("arial", 15), bg=bg_colour, fg="#FBFCFC").grid(row=0, column=0, padx=10, pady=30)
        # tea_item01_input = Entry(f3, font=("arial", 15), bd=5, width=15).grid(row=0, column=1, padx=4)

        # tea_item02 = Label(f3, text="Lemon Tea", font=("arial", 15), bg=bg_colour, fg="#FBFCFC").grid(row=1, column=0, padx=10, pady=30)
        # tea_item02_input = Entry(f3, font=("arial", 15), bd=5, width=15).grid(row=1, column=1, padx=4)

        # tea_item03 = Label(f3, text="Masala Chai", font=("arial", 15), bg=bg_colour, fg="#FBFCFC").grid(row=2, column=0, padx=10, pady=30)
        # tea_item03_input = Entry(f3, font=("arial", 15), bd=5, width=15).grid(row=2, column=1, padx=4)

        # tea_item04 = Label(f3, text="Black Tea", font=("arial", 15), bg=bg_colour, fg="#FBFCFC").grid(row=3, column=0, padx=10, pady=30)
        # tea_item04_input = Entry(f3, font=("arial", 15), bd=5, width=15).grid(row=3, column=1, padx=4)

        # tea_item05 = Label(f3, text="Herbal Tea", font=("arial", 15), bg=bg_colour, fg="#FBFCFC").grid(row=4, column=0, padx=10, pady=30)
        # tea_item05_input = Entry(f3, font=("arial", 1), bd=5, width=15).grid(row=4, column=1, padx=4)

        #---------------Bill Frame widget---------------
        f4 = Frame(self.window, bd=7, relief=GROOVE)
        f4.place(x=910, y=190, relwidth=0.39, height=500)

        bill_title = Label(f4, text="BILL", font=("arial",20,"bold"), bd=7, relief=GROOVE, bg="#CCD1D1").pack(fill=X)

        scroll_y = Scrollbar(f4, orient=VERTICAL)
        self.textarea = Text(f4, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(side=LEFT, fill=BOTH)

        # ---------------last buttons---------------

        f5 = Frame(self.window, bg=bg_colour, bd=7, relief=GROOVE)
        f5.place(x=0, y=690, relwidth=1, height=90)

        btn1 = Button(f5, text="Generate Bill", font=("arial",15), bd=5, relief=GROOVE, width=20, bg="#28B463")
        btn1.grid(row=0, column=0, padx=130, pady=17)

        btn2 = Button(f5, text="Clear", font=("arial", 15), bd=5, relief=GROOVE, width=20, bg="#F4D03F")
        btn2.grid(row=0, column=1, padx=130, pady=17)

        btn3 = Button(f5, text="Exit", font=("arial", 15), bd=5, relief=GROOVE, width=20, bg="#E74C3C")
        btn3.grid(row=0, column=2, padx=130, pady=17)

window = Tk()

obj = Bill_App(window)

window.mainloop()
