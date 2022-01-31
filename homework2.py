#Classwork 2
#Build a single bank app
#users can:
#-sign up with account number generated
#-login
#-withdraw
import random

def accountnumbergeneration():
    return random.randrange(1111111111,9999999999)
def login():
    print("Login")

def register():
    print("Register")

email = input("type your email address: ")
first_name = input("type your first name: ")
surname = input("type your surname: ")
password = input("type your password: ")

account_number = accountnumbergeneration()

database[account_number] = [email,first_name,surname,password]

print("Account successfully created!")