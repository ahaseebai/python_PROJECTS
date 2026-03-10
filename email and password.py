#program to update your email and password 
email=input("Type here email: ")
password=input("Type here password: ")
print(f'your email is: {email} \nyour password is: {password}')
value=input("you have to update email or password if you want: \npress yes otherwise no")
if value == "yes":
    email=input('update your email: ')
    password=input('update your password: ')
    print(f'your updated email is: {email}\nyour updated password is: {password}')

else:
    print("so you don't want to update your email and password! have a great day")