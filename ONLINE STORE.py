items=[]
fruits=['apple','mango','banana'] 
vegetables=['potato','tomato','Onion']
a=int(input("-------------------------ONLINE STORE-------------------------\npress\n1 for vegetable\n2 for fruits\n-1 for Exiting program\nType Accordingly:  "))
while a!=-1:
    if a==1:
        items.extend(vegetables)
        for x in items:
            print(x)
        ask= input("Do you want to buy : press--> yes/no ")
        if ask == 'yes':
            while True :
                b=input("what would you want to Buy! ")
                if b in vegetables:
                    print(f'{b} is Sucessfully Ordered')
                else:
                    print("this product is out of Stock")
                ask= input("Do you want to buy more : press--> yes/no ")
                if ask == 'no':
                    break
        
    elif a==2:
        items.extend(fruits)
        for x in items:
            print(x)
        ask= input("Do you want to buy : press--> yes/no ")
        if ask == 'yes':
            while True :
                b=input("what would you want to Buy! ")
                if b in fruits:
                    print(f'{b} is Sucessfully Ordered')
                else:
                    print("this product is out of Stock")
                ask= input("Do you want to buy more : press--> yes/no ")
                if ask == 'no':
                    break
    a=int(input("\n-------------------------ONLINE STORE-------------------------\npress\n1 for vegetable\n2 for fruits\n-1 for Exiting program\nType Accordingly:  "))
print("you are exiting the program and dont want to order any thing So, Go Home")

