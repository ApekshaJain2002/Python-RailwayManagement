import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',passwd='root',database='railway')
mycursor=mydb.cursor()
def menu():
    n=1
    while n>=1 and n<6:
        print()
        print("-"*50)
        print("RAILWAY MANAGEMENT SYSTEM")
        print("-"*50)
        print("1. TRAIN MANAGEMENT")
        print("2. RESERVATION OF TICKET")
        print("3. PASSANGER MANAGEMENT")
        print("4. CANCELLATION OF TICKET")
        print("5. Exit")
        n=int(input("ENTER YOUR CHOICE"))
        if n==1:
            train_details()
        elif n==2:
            reservation()
        elif n==3:
            passanger_details()
        elif n==4:
            cancel_ticket()
        elif n==5:
            print("YOU HAVE ENDED THE FUNCTION")
            exit()
        #else:
            #print("INVALID OPTION")
#######################################################
def train_details():
    ch='y'
    while ch=='y':
        print("1. ADD TRAIN")
        print("2. MODIFY ANY TRAIN DETAIL")
        print("3. DELETE ANY TRAIN DETAIL")
        print("4. SHOW ANY ONE TRAIN DETAIL")
        print("5. SHOW ALL TRAINS DETAIL")
        print("6. BACK TO MENU")
        n=int(input("ENTER YOUR CHOICE"))
        if n==1:
            add_train()
        elif n==2:
            modify_train()
        elif n==3:
            delete_train_detail()
        elif n==4:
            showone_train_detail()
        elif n==5:
            showall_train_details()        
        elif n==6:
            menu()
        else:
            print("INVALID OPTION")
        ch=input("DO YOU WANT TO CONTINUE y/n") 
##################################################             
def add_train():
    tnum=int(input("ENTER TRAIN'S NUMBER"))
    tname=input("ENTER TRAIN'S NAME")
    source=input("ENTER TRAIN'S SOURCE")
    destination=input("ENTER TRAIN'S DESTINATION")
    ac1=int(input("ENTER NUMBER OF SEATS AVAILABLE FOR FIRST CLASS"))
    ac2=int(input("ENTER NUMBER OF SEATS AVAILABLE FOR SECOND CLASS"))
    slp=int(input("ENTER NUMBER OF SEATS AVAILABLE FOR SLEEPER CELL"))
    fare_ac1=int(input("ENTER FARE FOR PER SEAT OF AC1"))
    fare_ac2=int(input("ENTER FARE FOR PER SEAT OF AC2"))
    fare_slp=int(input("ENTER FARE FOR PER SEAT OF SLEEPER CELL")) 
    mycursor.execute("insert into train_details values({},'{}','{}','{}',{},{},{},{},{},{})".format(tnum,tname,source,destination,ac1,ac2,slp,fare_ac1,fare_ac2,
                                                                                                    fare_slp))
    mydb.commit()
    print("-"*50)
    print("TRAIN ADDED SUCCESSFULLY")
    print("-"*50)
#########################################################################
def modify_train():
    tnum=int(input("ENTER TRAIN NUMBER OF TRAIN YOU WANT TO MODIFY"))
    mycursor.execute("select * from train_details")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        if x[0]==tnum:
            ch='y'
            while ch=='y':
                print("1. TO MODIFY NAME OF THE TRAIN ")
                print("2. TO MODIFY SOURCE OF THE TRAIN")
                print("3. TO MODIFY DEATINATION OF THE TRAIN ")
                print("4. TO MODIFY NUMBER OF SEAT FOR AC1")
                print("5. TO MODIFY NUMBER OF SEAT FOR AC2")
                print("6. TO MODIFY NUMBER OF SEAT FOR SLEEPER CELL ")
                ch=int(input("ENTER YOUR CHOICE"))
                if ch==1:
                    tname=input("ENTER THE NAME OF THE TRAIN YOU WANT TO MODIFY")
                    query="update train_details set tname='{}'where tnum={}".format(tname,tnum)
                    mycursor.execute(query)
                    mydb.commit()
                    print("TRAIN NAME MODIFIED SUCCESSFULLY")
                elif ch==2:
                    source=input("ENTER THE NEW SOURCE ")
                    query="update train_details set source='{}'where tnum={}".format(source,tnum)
                    mycursor.execute(query)
                    mydb.commit()
                    print("TRAIN SOURCE MODIFIED SUCCESSFULLY")
                elif ch==3:
                    destination=input("ENTER THE NEW DESTINATION ")
                    query="update train_details set destination='{}'where tnum={}".format(destination,tnum)
                    mycursor.execute(query)
                    mydb.commit()
                    print("TRAIN DESTINATION MODIFIED SUCCESSFULLY")
                elif ch==4:
                    ac1=input("ENTER THE NO OF SEATS FOR AC1")
                    query="update train_details set AC1='{}'where tnum={}".format(ac1,tnum)
                    mycursor.execute(query)
                    mydb.commit()
                    print("AC1 SEATS MODIFIED SUCCESSFULLY")
                elif ch==5:
                    ac2=input("ENTER THE NO OF SEATS FOR AC2")
                    query="update train_details set AC2='{}'where tnum={}".format(ac2,tnum)
                    mycursor.execute(query)
                    mydb.commit()
                    print("AC2 SEATS MODIFIED SUCCESSFULLY")
                elif ch==6:
                    slp=input("ENTER NO OF SEATS FOR SLEEPER")
                    query="update train_details set slp='{}'where tnum={}".format(slp,tnum)
                    mycursor.execute(query)
                    mydb.commit()
                    print("SEATS MODIFIED SUCCESSFULLY")
                else:
                    print("WRONG CHOICE")
                ch=input("DO YOU WANT TO CONTINUE")
                
               
#############################################################################
def delete_train_detail():
    tnum=int(input("ENTER THE TRAIN NUMBER YOU WANT TO DELETE "))
    mycursor.execute("select * from train_details")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        if x[0]==tnum:
            mycursor.execute("delete from train_details where tnum={}".format(tnum))
            mydb.commit()
            print("TRAIN DELETED SUCCESSFULLY")
        else:
            print("NO SUCH TRAIN FOUND")
############################################################################
def showone_train_detail():
    tnum=int(input("enter train's number of the train you want detail"))
    mycursor.execute("select * from train_details")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        if x[0]==tnum:
            print()
            print("train details of ",x[0])
            print("train name",x[1])
            print("source",x[2])
            print("destination",x[3])
            print("AC1 seats available",x[4])
            print("AC2 seats available",x[5])
            print("SLEEPER seats available",x[6])
            print("fare per seat of ac1 ",x[7])
            print("fare per seat of ac2 ",x[8]) 
            print("fare per seat of sleeper ",x[9]) 
################################################################################
def showall_train_details():
    print("all train details")         
    mycursor.execute("select * from train_details")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print()
        print("train details of ",x[0])
        print("train name",x[1])
        print("source",x[2])
        print("destination",x[3])
        print("AC1 seats available",x[4])
        print("AC2 seats available",x[5])
        print("SLEEPER seats available",x[6])
        print("fare per seat of ac1 ",x[7])
        print("fare per seat of ac2 ",x[8]) 
        print("fare per seat of sleeper ",x[9]) 
        
        
###################################################################################           
#########################################################################
def reservation():
################################################################################         
    pnr_no=int(input("enter pnr no"))
    p_name=input("enter passanger's name")
    age=int(input("enter age of person"))
    gender=input("enter your gender: M or F or OTHERS")
    address=input("enter your address")
    source='0'
    destination='0'
    t_name='0'
    status='0'
    print("choose the train you want to travel in")
    mycursor.execute("select tnum,tname,source,destination from train_details")
    myrecords=mycursor.fetchall()
    print("| train number |  train name  |  source | destination  |")
    for x in myrecords:
        print("|", x[0] ,"|" , x[1],"|", x[2] ,"|", x[3],"|")
    tnum=int(input("enter train no from above info"))
    for x in myrecords:
        if tnum==x[0]:
            t_name=x[1]
            print(" train's name",t_name)
            source=x[2]
            print("source",source)
            destination=x[3]
            print("destination",destination)
            status='waiting'
            if source!=destination:
                print("status converted from waiting to confirmed")
                status='confirmed'
            else :
                print ("sorry you cannot travel there")  
    nos_booked=int(input("enter no of seats you want to book"))
    print("select a class you would like to travel in")
    print("1.AC1 first class")
    print("2.AC2 second class")
    print("3.AC3 sleeper cell")
    ch=int(input("enter your choice"))
    if ch==1:
        cls='AC1'
        fare=nos_booked*1000

    elif ch==2:
        cls='AC2'
        fare=nos_booked*800
    elif ch==3:
        cls='AC3'
        fare=nos_booked*350
    else:
        print("invalid option")
    print("total amount to be paid",fare)
    
    query="insert into passanger_details values({},'{}',{},'{}','{}','{}','{}','{}',{},'{}','{}',{})".format(pnr_no,p_name,age,gender,address,t_name,source,destination
                                                                                                             ,nos_booked,cls,status,fare)
    mycursor.execute(query)
    mydb.commit()
    print("BOOKING completed")
    print("go back to menu")
##############################################################################
def passanger_details():
    print("1.modify passanger details")
    print("2.showone detail of passangers")
    print("3.show all details of passangers")
    n=int(input("enter your choice"))
    if n==1:
        modify_passangerdetails()
    elif n==2:
        showone_passangerdetail()
    elif n==3:
        showall_passangerdetails()
    else:
        print("INVALID OPTION")
###############################################################################
def modify_passangerdetails():
    pnr_no=int(input("enter PNR number of the passanger you want to modify"))
    mycursor.execute("select * from passanger_details")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        if x[0]==pnr_no:
            ch='y'
            while ch=='y':
                print("1. to modify name of the passanger")
                print("2. to modify age of the passanger")
                print("3. to modify gender of the passanger")
                print("4. to modify address of the passanger")
                ch=int(input("enter your choice"))
                if ch==1:
                    p_name=input("enter the name of passanger")
                    query="update passanger_details set p_name='{}'where pnr_no={}".format(p_name,pnr_no)
                    mycursor.execute(query)
                    mydb.commit()
                    print("passanger's name modified successfully")
                elif ch==2:
                    age=int(input("enter the age of passanger "))
                    query="update passanger_details set age={} where pnr_no={}".format(age,pnr_no)
                    mycursor.execute(query)
                    mydb.commit()
                    print("passanger's age modified successfully")
                elif ch==3:
                    gender=input("enter the gender of passanger ")
                    query="update passanger_details set gender='{}'where pnr_no={}".format(gender,pnr_no)
                    mycursor.execute(query)
                    mydb.commit()
                    print("passanger's gender modified successfully")
                elif ch==4:
                    address=input("enter the address of passanger")
                    query="update passanger_details set address='{}'where pnr_no={}".format(address,pnr_no)
                    mycursor.execute(query)
                    mydb.commit()
                    print("address modified successfull")
                else:
                    print("no such pssanger found")
                ch=input("do you want to continue yes or no")
            else:
                print("go back to menu")
        #else:
            #print("no such train found")
###################################################################
def showone_passangerdetail():
    pnr_no=int(input("enter PNR number"))
    mycursor.execute("select * from passanger_details")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        if x[0]==pnr_no:
            print()
            print("-"*50)
            print("passanger details of ",x[1])
            print("pnr_no",x[0])
            print("age",x[2])
            print("gender",x[3])
            print("address",x[4])
            print("train name",x[5])
            print("source",x[6])
            print("destination",x[7]) 
            print("nos_booked",x[8])
            print("class you choose",x[9])
            print("status",x[10])
            print("fare for seats",x[11])
        else:
            print("no such passanger")
################################################################################
def showall_passangerdetails():
    print("ALL PASSANGERS DETAILS")
    mycursor.execute("select * from passanger_details")
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print()
        print("passanger details of ",x[1])
        print("pnr_no",x[0])
        print("age",x[2])
        print("gender",x[3])
        print("address",x[4])
        print("train name",x[5])
        print("source",x[6])
        print("destination",x[7]) 
        print("nos_booked",x[8])
        print("class you choose",x[9])
        print("status",x[10])
        print("fare for seats",x[11]) 
        
################################################################################             
def cancel_ticket():
    print("ticket cancel window")
    pnr_no=int(input("enter PNR for cancellation of ticket"))
    query1="select * from passanger_details where pnr_no={}".format(pnr_no)
    mycursor.execute(query1)
    myrecords=mycursor.fetchall()
    for x in myrecords:
        print(x)
        if x[0]==int(pnr_no):
            print("you have a booking")
            choice=int(input("are you sure you want to cancel the ticket,enter 1 for yes ,or 2 for no "))
            if choice==1:
                query2="update passanger_details set status='cancelled' where pnr_no={}".format(pnr_no)
                mycursor.execute(query2)
                mydb.commit()
                print("cancellation completed")

            else:
                print("you still have a reservation")
        #else:
            #print(" you are not having any registration")         
                
    
    print("Go back to menu")

menu()

