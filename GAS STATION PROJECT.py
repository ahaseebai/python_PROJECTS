def cng():
    name =input("What is your name: ")
    fuel=int(input("How much kilo of CNG you want to fill the Tank in Your vehicle: "))     
    ccng=150
    total=float(fuel*ccng)
    print(f'Mr : {name} \n{fuel} killo of CNG has Successfully filled in Your vehicle Tank\nYour total charges are : {total} with respect to {str(ccng)} per Kilo\n')

def petrol():
    name =input("What is your name: ")
    fuel=int(input("How much litre you want to fill the Tank in Your vehicle: "))
    petrol=250
    total=float(fuel*petrol)
    print(f'Mr : {name} \n{fuel} liters of Petrol has Successfully filled in Your vehicle Tank\nYour total charges are : {total} with respect to {str(petrol)} per litre\n')


def diesel():
    name =input("What is your name: ")
    fuel=int(input("How much litre you want to fill the Tank in Your vehicle: "))
    diesel=300
    total=float(fuel*diesel)
    print(f'Mr : {name} \n{fuel} liters of Diesel has Successfully filled in Your vehicle Tank\nYour total charges are : {total}  with respect to {str(diesel)} per litr\n')

flag=True
while flag:
    choice=int (input("WELCOME TO GAS STATION\nPress\n1----> PETROL\n2-----> CNG\n3-----> DIESEL\n4------> EXIT\n"))
    if choice ==1:
        petrol()
    elif choice ==2 :
        cng()
    elif choice == 3:
        diesel()
    elif choice== 4:
        print("you are exiting : gareeb pesa ghra khareenchy a na!\n")
    ask=input("Press yes if you want to continue otherwise no: ")
    print("_____________________________________________________\n")
    if ask=='no'or choice==4:
        flag = False




