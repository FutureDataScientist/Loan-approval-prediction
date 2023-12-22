
import pandas as pd
from categoricalVar import typeOfLoanList,occupationList,creditMixList,paymentOfMinAmountList,paymentBehaviorList
from sklearn.model_selection import train_test_split
import tkinter
from tkinter import *
from sklearn.ensemble import RandomForestClassifier


root = Tk()
root.geometry("650x750")
root.title("Loan Prediction")
# root.resizable(False,False)

# tkinter variable for storing entries

monthvalue = IntVar(value="")
agevalue = IntVar(value="")
annualincomevalue = IntVar(value="")
monthlyinhandsalaryvalue = IntVar(value="")
numberbankaccountvalue = IntVar(value="")
numbercreditcardvalue = IntVar(value="")
interestratevalue = IntVar(value="")
numberofloanvalue = IntVar(value="")
delayfromduedatevalue = IntVar(value="")
numberofdelayedpaymentvalue = IntVar(value="")
changedcreditlimitvalue = IntVar(value="")
numbercreditinquiriesvalue = IntVar(value="")
outstandingdebtvalue = IntVar(value="")
creditutilizationratiovalue = IntVar(value="")
credithistoryagevalue = IntVar(value="")
totalemipermonthvalue = IntVar(value="")
amountinvestedmonthlyvalue = IntVar(value="")
monthlybalancevalue = IntVar(value="")
creditscorevalue = IntVar(value="")
waitingVar = IntVar(value="")

occupationClicked= StringVar()
creditMixClicked= StringVar()
paymentOfMinClicked= StringVar()
paymentBehaviorClicked= StringVar()
typeOfLoanClicked= StringVar()

def dataValidation():
    try:
        if monthvalue.get()<=0 or monthvalue.get()>12:
            showResult.config(text="please enter the month only  1 to 12",fg="red")
            return
        elif agevalue.get()<=0 or agevalue.get()>80:  
            showResult.config(text="please enter the  age only 1 to 80",fg="red")
            return
        
        kl=[annualincomevalue.get(),monthlyinhandsalaryvalue.get(),numberbankaccountvalue.get(),numbercreditcardvalue.get(),interestratevalue.get(),numberofloanvalue.get(),delayfromduedatevalue.get(),numberofdelayedpaymentvalue.get(),outstandingdebtvalue.get(),creditutilizationratiovalue.get(),credithistoryagevalue.get(),totalemipermonthvalue.get(),amountinvestedmonthlyvalue.get(),monthlybalancevalue.get(),numbercreditinquiriesvalue.get(),changedcreditlimitvalue.get() ]     
        for i in kl:
            if isinstance(i,str):
                showResult.config(text="please enter the numeric value",fg="red")
                return
        if (int(monthlyinhandsalaryvalue.get()))>(int(annualincomevalue.get())/12):
            showResult.config(text="your monthly inhand salary\n greater than annualincome",fg="red")
            return
        elif (int(monthlybalancevalue.get()))>(int(monthlyinhandsalaryvalue.get())):
            showResult.config(text="your monthly balance greater\n than your monthly in hand salary",fg="red")
            return
        elif (int(monthlyinhandsalaryvalue.get()))<=(int(totalemipermonthvalue.get())):
            showResult.config(text="your total emi per month\n value greater than monthly in hand salary",fg="red")
            return
        elif (int(monthlyinhandsalaryvalue.get()))<=(int(amountinvestedmonthlyvalue.get())):
            showResult.config(text="your amount invested monthly \n  greater than your monthly in hand salary",fg="red")
            return
    except:
        showResult.config(text="please enter the numeric value",fg="red")
        return
    predict()
            




# END VAR DECELERATION

classifier=RandomForestClassifier(n_estimators=800,random_state=0)
def modelBuild():
    global classifier
    loading.config(text="Please Wait Model is Loading...")
    root.after(1000, waitingVar.set, 1)
    root.wait_variable(waitingVar)
    df=pd.read_csv("cleanLoanData.csv",nrows=20000)
    real_x=df.drop("Credit_Score",axis=1)
    real_y=df["Credit_Score"]
    x_train, x_test, y_train, y_test = train_test_split(real_x, real_y, test_size=0.2, random_state=17,stratify=real_y)
    rf=RandomForestClassifier()
    classifier.fit(x_train,y_train)
    loading.grid_forget()

def predict():
    try:
        pred=classifier.predict([[
            int(monthvalue.get()),
            float(agevalue.get()),
            int(occupationList.index(occupationClicked.get())),
            float(annualincomevalue.get()),
            float(monthlyinhandsalaryvalue.get()),    
            float(numberbankaccountvalue.get()), 
            float(numbercreditcardvalue.get()),
            float(interestratevalue.get()),
            float(numberofloanvalue.get()),
            int(typeOfLoanList.index(typeOfLoanClicked.get())),
            float(delayfromduedatevalue.get()),
            float(numberofdelayedpaymentvalue.get()),
            float(changedcreditlimitvalue.get()),
            float(numbercreditinquiriesvalue.get()),
            int(creditMixList.index(creditMixClicked.get())),
            float(outstandingdebtvalue.get()),
            float(creditutilizationratiovalue.get()),
            float(credithistoryagevalue.get()),
            int(paymentOfMinAmountList.index(paymentOfMinClicked.get())),
            float(totalemipermonthvalue.get()),
            float(amountinvestedmonthlyvalue.get()),
            int(paymentBehaviorList.index(paymentBehaviorClicked.get())),
            float(monthlybalancevalue.get())]])
    except Exception as e:
        print(e)
    # 0 is Good Condition
    if pred[0]==0:
        showResult.config(text="PASS THE LOAN BUT \nTAKE SOME INFORMATION",fg="green")
    # 1 is Poor Condition
    elif pred[0]==1:
        showResult.config(text="NOT PASS THE LOAN",fg="red")
    # 2 is Standard Condition
    else:
        showResult.config(text="PASS THE LOAN",fg="green")





# loading
loading=Label(root,text="",fg="red", font=('Roboto',12,'bold'))
loading.grid(row=0,column=2,columnspan=5)
# heading
Label(root  ,text="Loan Prediction System" , font=('times new roman',30,'bold'),fg="blue", pady=15).grid(row=1,column=2,columnspan=5,sticky=E)

# show Result
showResult=Label(root,text="", font=('Roboto',15,'bold'))




#text for our form

month = Label(root, text = "Month", font= "comicsansms 10 ")
age = Label(root, text = "Age",font= "comicsansms 10 ")
occupation = Label(root, text = "Occupation",font= "comicsansms 10 ")
annualincome = Label(root, text = "Annual Income", font= "comicsansms 10 ")
monthlyinhandsalary = Label(root, text = "Monthly_Inhand_Salary", font= "comicsansms 10 ")
numberbankaccount = Label(root, text = "Num_Bank_Accounts", font= "comicsansms 10 ")
numbercreditcard = Label(root, text = "Num_Credit_Card", font= "comicsansms 10 ")
interestrate = Label(root, text = "Interest_Rate", font= "comicsansms 10 ")
numberofloan = Label(root, text = "Num_of_Loan", font= "comicsansms 10 ")
delayfromduedate = Label(root, text = "Delay_from_due_date", font= "comicsansms 10 ")
numberofdelayedpayment = Label(root, text = "Num_of_Delayed_Payment", font= "comicsansms 10 ")
typeofloan = Label(root, text = "Type_of_Loan", font= "comicsansms 10 ")
changedcreditlimit= Label(root, text = "Changed_Credit_Limit", font= "comicsansms 10 ")
numbercreditinquiries = Label(root, text = "Num_Credit_Inquiries", font= "comicsansms 10 ")
creditmix = Label(root, text = "Credit_Mix", font= "comicsansms 10 ")
outstandingdebt= Label(root, text = "Outstanding_Debt", font= "comicsansms 10 ")
creditutilizationratio= Label(root, text = "Credit_Utilization_Ratio", font= "comicsansms 10 ")
credithistoryage = Label(root, text = "Credit_History_Age", font= "comicsansms 10 ")
paymentofminamount = Label(root, text = "Payment_of_Min_Amount", font= "comicsansms 10 ")
totalemipermonth = Label(root, text = "Total_EMI_per_month", font= "comicsansms 10 ")
amountinvestedmonthly= Label(root, text = "Amount_invested_monthly", font= "comicsansms 10 ")
paymentbehaviour = Label(root, text = "Payment_Behaviour", font= "comicsansms 10 ")
monthlybalance= Label(root, text = "Monthly_Balance", font= "comicsansms 10 ")


#pack text for our form

month.grid(row=3,column=4,sticky='w')
age.grid(row=4,column=4,sticky='w')
occupation.grid(row=5,column=4,sticky='w')
annualincome.grid(row=6,column=4,sticky='w') 
monthlyinhandsalary.grid(row=7,column=4,sticky='w') 
numberbankaccount.grid(row=8,column=4,sticky='w') 
numbercreditcard.grid(row=9,column=4,sticky='w')
interestrate.grid(row=10,column=4,sticky='w')
numberofloan.grid(row=11,column=4,sticky='w')
typeofloan.grid(row=12,column=4,sticky='w')
delayfromduedate.grid(row=14,column=4,sticky='w')
numberofdelayedpayment.grid(row=15,column=4,sticky='w') 
changedcreditlimit.grid(row=16,column=4,sticky='w')
numbercreditinquiries.grid(row=17,column=4,sticky='w') 
creditmix.grid(row=18,column=4,sticky='w') 
outstandingdebt.grid(row=19,column=4,sticky='w')
creditutilizationratio.grid(row=20,column=4,sticky='w')
credithistoryage.grid(row=21,column=4,sticky='w') 
paymentofminamount.grid(row=22,column=4,sticky='w') 
totalemipermonth.grid(row=23,column=4,sticky='w') 
amountinvestedmonthly.grid(row=24,column=4,sticky='w')
paymentbehaviour.grid(row=25,column=4,sticky='w') 
monthlybalance.grid(row=26,column=4,sticky='w')



# entry for a form

monthentry = Entry(root , textvariable=monthvalue,bd=3,relief=GROOVE)
ageentry = Entry(root , textvariable=agevalue,bd=3,relief=GROOVE)
annualincomeentry = Entry(root , textvariable=annualincomevalue,bd=3,relief=GROOVE)
monthlyinhandsalaryentry = Entry(root , textvariable=monthlyinhandsalaryvalue,bd=3,relief=GROOVE)
numberbankaccountentry = Entry(root , textvariable=numberbankaccountvalue,bd=3,relief=GROOVE)
numbercreditcardentry = Entry(root , textvariable=numbercreditcardvalue,bd=3,relief=GROOVE)
interestrateentry = Entry(root , textvariable=interestratevalue,bd=3,relief=GROOVE)
numberofloanentry = Entry(root , textvariable=numberofloanvalue,bd=3,relief=GROOVE)
delayfromduedateentry = Entry(root , textvariable=delayfromduedatevalue,bd=3,relief=GROOVE)
numberofdelayedpaymententry = Entry(root , textvariable=numberofdelayedpaymentvalue,bd=3,relief=GROOVE)
changecreditlimitentry = Entry(root , textvariable=changedcreditlimitvalue,bd=3,relief=GROOVE)
numbercreditinquiriesentry = Entry(root , textvariable=numbercreditinquiriesvalue,bd=3,relief=GROOVE)
outstandingdebtentry = Entry(root , textvariable=outstandingdebtvalue,bd=3,relief=GROOVE)
creditutilizationratioentry = Entry(root , textvariable=creditutilizationratiovalue,bd=3,relief=GROOVE)
credithistoryageentry = Entry(root , textvariable=credithistoryagevalue,bd=3,relief=GROOVE)
totalemipermonthentry = Entry(root , textvariable=totalemipermonthvalue,bd=3,relief=GROOVE)
amountinvestedmonthlyvalueentry = Entry(root , textvariable=amountinvestedmonthlyvalue,bd=3,relief=GROOVE)
monthlybalanceentry = Entry(root , textvariable=monthlybalancevalue,bd=3,relief=GROOVE)

# pack entry
monthentry.grid(row=3,column=5,sticky='w')
ageentry.grid(row=4, column=5,sticky='w')
annualincomeentry.grid(row=6 , column=5,sticky='w')
monthlyinhandsalaryentry.grid(row=7 , column=5,sticky='w')
numberbankaccountentry.grid(row=8 , column=5,sticky='w')
numbercreditcardentry.grid(row=9,column=5,sticky='w')
interestrateentry .grid(row=10,column=5,sticky='w')
numberofloanentry.grid(row=11,column=5,sticky='w')
delayfromduedateentry.grid(row=14,column=5,sticky='w')
numberofdelayedpaymententry.grid(row=15,column=5,sticky='w')
changecreditlimitentry.grid(row=16,column=5,sticky='w')
numbercreditinquiriesentry.grid(row=17,column=5,sticky='w')
outstandingdebtentry.grid(row=19,column=5,sticky='w')
creditutilizationratioentry.grid(row=20,column=5,sticky='w')
credithistoryageentry.grid(row=21,column=5,sticky='w')
totalemipermonthentry.grid(row=23,column=5,sticky='w')
amountinvestedmonthlyvalueentry.grid(row=24,column=5,sticky='w')
monthlybalanceentry.grid(row=26,column=5,sticky='w')

#drop down box

def show1():
    mylabel1 = Label(root,text=occupationClicked.get(), font= "comicsansms 10",bd=3,relief=GROOVE).grid()
options=occupationList

occupationClicked.set(options[0])

drop = OptionMenu(root,occupationClicked,*options)
drop.grid(row=5,column=5,sticky='w')




def show2():
    mylabel2 = Label(root,text=creditMixClicked.get(), font= "comicsansms 10",bd=3,relief=GROOVE).grid()
options=creditMixList

creditMixClicked.set(options[0])

drop = OptionMenu(root,creditMixClicked,*options)
drop.grid(row=18,column=5,sticky='w')


def show3():
    mylabel3 = Label(root,text=paymentOfMinClicked.get(), font= "comicsansms 10",bd=3,relief=GROOVE).grid()
options=paymentOfMinAmountList

paymentOfMinClicked.set(options[0])

drop = OptionMenu(root,paymentOfMinClicked,*options)
drop.grid(row=22,column=5,sticky='w')

def show4():
    mylabel4 = Label(root,text=paymentBehaviorClicked.get(), font= "comicsansms 10",bd=3,relief=GROOVE).grid()
options=paymentBehaviorList

paymentBehaviorClicked.set(options[0])

drop = OptionMenu(root,paymentBehaviorClicked,*options)
drop.grid(row=25,column=5,sticky='w')

def show5():
    mylabel5 = Label(root,text=typeOfLoanClicked.get(), font= "comicsansms 10",bd=3,relief=GROOVE).grid()
options=['Auto Loan',
 'Auto Loan, Auto Loan, Auto Loan, and Home Equity Loan',
 'Auto Loan, Auto Loan, Auto Loan, and Not Specified',
 'Auto Loan, Auto Loan, Auto Loan, and Personal Loan',
 'Auto Loan, Auto Loan, Credit-Builder Loan, Not Specified, Not Specified, and Not Specified',
 'Auto Loan, Auto Loan, Credit-Builder Loan, and Credit-Builder Loan',
 'Auto Loan, Auto Loan, Credit-Builder Loan, and Debt Consolidation Loan',
 'Auto Loan, Auto Loan, Credit-Builder Loan, and Personal Loan',
 'Auto Loan, Auto Loan, Debt Consolidation Loan, Auto Loan, Not Specified, Personal Loan, and Credit-Builder Loan',
 'Auto Loan, Auto Loan, Debt Consolidation Loan, Home Equity Loan, Payday Loan, Credit-Builder Loan, and Credit-Builder Loan',
 'Auto Loan, Auto Loan, Debt Consolidation Loan, Payday Loan, Debt Consolidation Loan, Debt Consolidation Loan, and Not Specified',
 'Auto Loan, Auto Loan, Debt Consolidation Loan, Payday Loan, Mortgage Loan, Credit-Builder Loan, and Auto Loan',
 'Auto Loan, Auto Loan, Debt Consolidation Loan, Payday Loan, Payday Loan, and Personal Loan',
 'Auto Loan, Auto Loan, Debt Consolidation Loan, and Credit-Builder Loan',
 'Auto Loan, Auto Loan, Debt Consolidation Loan, and Not Specified',
 'Auto Loan, Auto Loan, Debt Consolidation Loan, and Student Loan',
 'Auto Loan, Auto Loan, Home Equity Loan, Credit-Builder Loan, Mortgage Loan, and Payday Loan',
 'Auto Loan, Auto Loan, Home Equity Loan, Home Equity Loan, Personal Loan, Payday Loan, and Personal Loan',
 'Auto Loan, Auto Loan, Mortgage Loan, Not Specified, Payday Loan, Personal Loan, and Payday Loan',
 'Auto Loan, Auto Loan, Mortgage Loan, and Mortgage Loan',
 'Auto Loan, Auto Loan, Not Specified, Debt Consolidation Loan, Not Specified, Credit-Builder Loan, Debt Consolidation Loan, and Personal Loan',
]

typeOfLoanClicked.set(options[0])
drop = OptionMenu(root,typeOfLoanClicked,*options)
drop.grid(row=12,column=5,sticky='w')


b1=Button(root,text="Prediction" , command=dataValidation,fg="green",bd=3,relief=GROOVE).grid(row=31,column=5,pady=10)
showResult.grid(row=33,column=2,columnspan=5)

modelBuild()


root.mainloop()