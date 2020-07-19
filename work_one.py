complete = False
user = {"malli" : "Malli2010", "nesh" : "1234" }
 
while not complete:
    username = input("Username: ")
    password = input("Password: ")
    if username == user and password == password:
        continue
    elif username not in user:
        print("This is not a valid username, input username again!")
        continue
    elif password != user[username]:
        
        print("Password is not valid for username.")
        continue
    elif password == user[username]:
        print("Welcome "+username)
        print("Thank you for logging on. ")
        complete = True
        print ("Username and Password Validated in Python")     
    elif password == user[username]:
        print("Welcome "+username)
        print("Thank you for logging in. ")
        complete = True  
def adding_name():
    with open('person.txt','a') as f:
        asa = input("Participant first name :  ")
        if asa == " ":
            print("enter a name")
            adding_name()
        else:
            second = input("Participant Second Name: ")
            if second == " ":
                print("enter a name")
                adding_name()
            else:
                f.write(asa)
                f.write(second)
                f.write("\n")
        
adding_name()


def pay():
    print("we have the following tickets. ")
    with open('tickets.txt','a') as f:   
        s = ('''
        1.ordinary
        2.V.I.P
        3.Golden

        ''')
        print(s)
        b = input("Choose one of the tickets : ")
        if b == " ":
            print("enter one of the tickets")
            pay()
        else:
            if b == 'ordinary' or b == 'Ordinary'or  b == '1':
                print("you have to pay 100ksh")
            elif b == 'V.I.P' or  b =='2'or  b == 'vip':
                print("you have to pay 1000ksh")
            elif b == 'Golden' or b == 'golden' or  b == '3':
                print("you have to pay 10000ksh")
pay()