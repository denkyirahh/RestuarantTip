# Author - Michael Asomani        Date - 11/22/21
# Purpose - Write a GUI program that calculates the tip 
# and total to pay at a restuarant

from tkinter import * 
 
class RestTipCalculator: 
    def __init__(self): 
        restTip_window = Tk()  # create a restTip_window 
        restTip_window.title("Restuarant Tip Calculator") 
        var = IntVar()
        self.tip_obj = IntVar() 
        
        # "Directions" to user
        Label(restTip_window, text = "Amount of the Bill ($)")\
            .grid(row = 1, column= 1,sticky = E) 
        Label(restTip_window, text = "Pick Tip Percentage")\
            .grid(row = 2,column= 2,sticky = E) 
        Radiobutton(restTip_window, text = "10%", variable=self.tip_obj, value=1)\
            .grid(row = 3,column= 1,sticky = E)
        Radiobutton(restTip_window, text = "15%", variable=self.tip_obj, value=2)\
            .grid(row = 3,column= 2,sticky = E) 
        Radiobutton(restTip_window, text = "18%", variable=self.tip_obj, value=3)\
            .grid(row = 3,column= 3,sticky = E) 
        Radiobutton(restTip_window, text = "20%", variable=self.tip_obj, value=4)\
            .grid(row = 3,column= 4,sticky = E) 
        Label(restTip_window, text = "Tip Calculated ($)").\
            grid( row = 5, column = 1, sticky = E) 
        Label(restTip_window, text = "Total Bill ($)").\
            grid( row = 6, column = 1, sticky = E) 
  
        # Input variables
        self.bill_obj = StringVar() 
        self.entry_bill = Entry(restTip_window, textvariable = self.bill_obj, \
            justify = RIGHT) 
        self.entry_bill.grid(row = 1, column = 2)  
        
        # Button to trigger the calculation of bill 
        btn_calculate = Button(restTip_window, text = "Calculate Bill", \
        command = self.calculate_bill) 
        btn_calculate.grid(row = 4, column = 2, sticky = E) 
 
        # Output variables
        self.tip_amount_obj = StringVar() 
        self.total_amount_obj = StringVar() 
         
        Label(restTip_window, textvariable = self.tip_amount_obj).\
            grid(row = 5, column = 2, sticky = E) 
        Label(restTip_window, textvariable = self.total_amount_obj).\
            grid(row = 6, column = 2, sticky = E) 
 
        self.entry_bill.bind('<KeyPress-Return>', self.start_computations) 
        btn_calculate.bind('<KeyPress-Return>', self.start_computations) 
        self.entry_bill.focus_set() 
        restTip_window.mainloop() 
 
    def calculate_bill(self): 
        # get data from the GUI 
        if self.any_null_entries(): # if entry is null, it will kick us out of this method too 
            return # get out now 
        flt_bill = float(self.bill_obj.get()) 
        flt_tip  = float(self.tip_obj.get() ) 
         
        # call helping function to compute tip amount, then compute total bill
        tip_amount = self.compute_tip_amount(flt_bill) 
        total_amount = flt_bill + tip_amount
         
        # place results back into labels on the GUI 
        self.tip_amount_obj.set(format(tip_amount, "10.2f")) 
        self.total_amount_obj.set(format(total_amount, "10.2f")) 
 
    def compute_tip_amount(self, bill): 
        choice  = self.tip_obj.get()
        if choice == 1:         # 10% percentage tip
            tip_perc = 0.10
        elif choice == 2:       # 15% percentage tip
            tip_perc = 0.15
        elif choice == 3:       # 18% percentage tip
            tip_perc = 0.18
        elif choice == 4:       # 20% percentage tip
            tip_perc = 0.20
        else:
            messagebox.showerror("Tip Error", "Tip percentage not given") 
            self.tip_obj.focus_set()  
            
        tip_amount = tip_perc * bill 
        return tip_amount 
 
    def start_computations(self, keypress): 
        self.calculate_bill() 
 
    def any_null_entries(self): 
        input_str = self.bill_obj.get() 
        if input_str == '': 
            messagebox.showerror("Bill Error", "Bill not given") 
            self.entry_bill.focus_set() 
            return True 
 
RestTipCalculator()  # create GUI