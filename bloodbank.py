#CBSE Computer Science Project, 28-06-2024
'''HARSH AGARWAL, S7C AND IBRAHIM ABDUR RAZZAK, S7C'''
'''This project is to demonstrate a menu cum database based program for bloodbanks,
to record the details of donors'''

import mysql.connector as mc
import random as rand
MyDB = mc.connect(host='localhost',user='root',password='harsh1234')

MC= MyDB.cursor()

MC.execute("CREATE DATABASE IF NOT EXISTS bloodbank;")
MC.execute('use bloodbank;')
MC.execute('CREATE TABLE IF NOT EXISTS DETAILS(id INT PRIMARY KEY,name VARCHAR(100) NOT NULL, dob date, aadhaarno varchar(12), bg varchar(3), lastdon date, HN_city varchar(100), state varchar(100), country varchar(100), mobno varchar(50), email varchar(100),TEMPDATE DATE);')
MC.execute('CREATE TABLE IF NOT EXISTS Hist(id INT, DonHist DATE);')

def CheckEleg(N):
    print("To be eligible for donating blood: ")
    print("You need to have atleast a three month gap between the new date and last donation.")
    LDDN=input("Enter new date you would like to have your donation on(Enter in DD-MM-YYYY format ONLY): ")
    LDDN1=LDDN.split('-')
    LDDN2=LDDN1[2]+'-'+LDDN1[1]+'-'+LDDN1[0]
    MC.execute("UPDATE DETAILS SET TEMPDATE=%s where id=%s;",(LDDN2,N))
    MyDB.commit()
    MC.execute("SELECT DATEDIFF(TEMPDATE,lastdon) FROM DETAILS WHERE id=%s;",(N,))
    R=MC.fetchall()
    if R[0][0]>=90:
        print("You are eligible for donating blood.")
        print("Your new appointment date has been recorded.")
        print("Make sure to contact your nearest bloodbank for more details, and reach on time!")
        MC.execute("UPDATE DETAILS SET lastdon=%s where id=%s;",(LDDN2,N))
        MyDB.commit()
        MC.execute("UPDATE DETAILS SET TEMPDATE=%s where id=%s;",(N,None))
        MyDB.commit()
        MC.execute("INSERT INTO HIST VALUES(%s,%s);",(N,LDDN2))
        MyDB.commit()

    else:
        print("You are not eligible to donate blood yet.")
        print("You should have atleast 3 months of gap from your last donation.")

def Modify(N):
    print("Please write 0 wherever you dont want to update: ")
    AN=int(input("Enter new Aadhar No.: "))
    NN=input("Enter new name: ")
    A1N=input("Enter new House Number and city: ")
    SN=input('Enter new State: ')
    CN=input("Enter new country: ")
    MN1=int(input("Enter new Mobile number: "))
    EN=input("Enter new email: ")

    if AN!=0:
        C3="UPDATE DETAILS SET aadhaarno=%s where id=%s;"
        V3=(AN,N)
        MC.execute(C3,V3)
        MyDB.commit()
    if NN!="0":
        C4="UPDATE DETAILS SET NAME=%s where id=%s;"
        V4=(NN,N)
        MC.execute(C4,V4)
        MyDB.commit()
    if A1N!="0":
        C5="UPDATE DETAILS SET HN_city=%s where id=%s;"
        V5=(A1N,N)
        MC.execute(C5,V5)
        MyDB.commit()
    if SN!="0":
        C7="UPDATE DETAILS SET STATE=%s where id=%s;"
        V7=(SN,N)
        MC.execute(C7,V7)
        MyDB.commit()
    if CN!="0":
        C8="UPDATE DETAILS SET COUNTRY=%s where id=%s;"
        V8=(CN,N)
        MC.execute(C8,V8)
        MyDB.commit()
    if MN1!=0:
        C9="UPDATE DETAILS SET mobno=%s where id=%s;"
        V9=(MN1,N)
        MC.execute(C9,V9)
        MyDB.commit()
    if EN!="0":
        C11="UPDATE DETAILS SET email=%s where id=%s;"
        V11=(EN,N)
        MC.execute(C11,V11)
        MyDB.commit()

def Search(X):
    C2="SELECT * FROM DETAILS WHERE bg=%s;"
    V2=(X,)
    MC.execute(C2,V2)
    R=MC.fetchall()
    if len(R)!=0:
        for i in R:
            print("ID:",i[0])
            print("Aadhaar No.:",i[3])
            print("Blood Group:",i[4])
            print("Last date of Donation:",i[5])
            print("Name:",i[1])
            print("Date of Birth:",i[2])
            print("House number and City:",i[6])
            print("State:",i[7])
            print("Country:",i[8])
            print("Mobile Number:",i[9])
            print("Email:",i[10])
        print("Total no. of matching Rows: ",MC.rowcount)
    else:
        print("No donors with specified Blood Group found!")


print("Options:\n1.Enter a donor's details\n2.Remove a donor's details\n3.Display list of donors and details\n4.Modify a donor's details\n5.Show list of all donor's of a blood type\n6.Check eligibility of a donor\n7.View Donor history of particular donor\n8.Quit the program")

choice=0
while choice!="8":
    choice = input('Enter choice:')
    if choice=="1":
        name = input('Enter donor name:')
        dob = input('Enter date of birth in yyyy-mm-dd format:')
        aadhaarno=int(input('Enter Aadhaar Number:'))
        #blood type is bg
        bg = input('Enter blood group/type:')
        lastdon = input('Enter last date of donation in yyyy-mm-dd format:')
        city = input('Enter city:')
        state = input('Enter state:')
        country = input('Enter country:')
        mobno = int(input('Enter mobile number of donor:'))
        email = input('Enter email of donor:')
        id1=""
        for i in range(5):
            x=rand.randint(0,9)
            id1+=str(x)
        id2=int(id1)
        print("The unique id of the person is:",id2)

        donordet= (id2, name, dob, aadhaarno, bg, lastdon, city, state, country ,mobno, email, None)

        cmnd='INSERT INTO DETAILS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'

        MC.execute(cmnd,donordet)
        MC.execute("INSERT INTO HIST VALUES(%s,%s);",(id2,lastdon))
        MyDB.commit()

    elif choice=="2":
        print("Enter the donor's id you would like to delete: ")
        removeid= int(input("Enter donor's ID:"))
        MC.execute('DELETE FROM DETAILS WHERE id=%s;',(removeid,))
        MyDB.commit()

    elif choice=="3":
        MC.execute("SELECT * FROM DETAILS")
        donors = MC.fetchall()

        if MC.rowcount==0:
            print("No donors found.")
        else:
           print("\nList of Donors:")
           for i in donors:
            print("ID:",i[0])
            print("Aadhaar No.:",i[3])
            print("Blood Group:",i[4])
            print("Last date of Donation:",i[5])
            print("Name:",i[1])
            print("Date of Birth:",i[2])
            print("House number and City:",i[6])
            print("State:",i[7])
            print("Country:",i[8])
            print("Mobile Number:",i[9])
            print("Email:",i[10])
        print("Total no. of matching Rows: ",MC.rowcount)

    elif choice=="4":
        X=int(input("Enter id of the person whose details you would like to modify: "))
        Modify(X)
    
    elif choice=="5":
        Y=input("Enter the blood group of person you would like to search: ")
        Search(Y)
    
    elif choice=="6":
        Z=int(input("To check your elgibility of donation, please enter your id: "))
        CheckEleg(Z)

    elif choice=="7":
        VD=int(input("Enter donor's id whose donation history you would like to view: "))
        MC.execute("SELECT * FROM Hist where id=%s;",(VD,))
        R=MC.fetchall()
        print("Donation history for",VD,":")
        for i in R:
            print(i[1])

    elif choice=="8":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid option!Please choose another option!")

