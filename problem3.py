#! python3

"""
 Have the user enter a username 
 If the username is not "admin" then tell them it is an "invalid user", 
 but if it is, then ask them for a password 
 If they get the password correct (password is 12345password) 
 then display the message "Access granted"
 remember to use .strip() when retrieving strings or you will
 include hidden characters (the carriage return) that will
 not match
 1 marks

 Example:
 Enter username: admin
 Enter password: 12345password
 Access granted

 Enter username: notadmin
 invalid user

 Enter username: admin
 Enter password: password
 Access denied
"""

def login():  
    username = input("Enter username: ")  
    password = input("Enter password: ")  
  
    valid_users = ["admin"]  
    valid_passwords = ["12345password"]  
  
    if username in valid_users and password == valid_passwords[valid_users.index(username)]:  
        print("Access granted")  
    
    if valid_users !=["admin"] :  
        print("Invalid username")  
        
    elif valid_passwords !=("12345password"):
        print("Access Deneid")

login()  



"""
b=("12345password")
a=input("enter username")
if (a)==("admin"):
   b= input("password:")
elif b ==("12345password"):
    print("access granted")

"""