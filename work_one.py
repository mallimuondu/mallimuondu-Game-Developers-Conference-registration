from tinydb import TinyDB,Query
import datetime as time
def datetieme():
    now = time.datetime.now()
    hour = now.hour
    if hour < 12:
        greating =  "Good morning"
    elif hour > 12 and hour < 17:
        greating =  "Good afternoon"

    elif hour > 17 and hour < 19:
        greating =  "Good evening"
    else:
        greating = 'Good night'
    print(greating)
datetieme()


def login():
    complete = False
    user = {"malli" : "Malli2010", "Nesh" : "1" }

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
            print("Welcome username ")
            print("Thank you for logging on. ")
            complete = True
            print ("Username and Password Validated in Python")     
login()
def adding_name():
    asa = input("enter first name")
    second = input("Participant Second Name: ") 
    name3 = asa + second
    if name3 == "":
        print("enter a name")
    
    else:
        dicti = {"name1":asa, "name2":second}
        db = TinyDB('people.json')
        db.insert(dicti)
adding_name()
def pay():
    print("we have the following tickets. ")
    s = ('''
    1.ordinary
    2.V.I.P
    3.Golden
    ''')
    print(s)
    with open('tickets.txt','a') as f: 
        b = input("Choose one of the tickets : ")
        f.write(b)
        f.write("\n")
        if b == "":
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