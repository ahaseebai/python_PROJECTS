pizza=['Crown Crust Pizza','Behari Kabab Pizza','Chicken Fajita Pizza','Chicken Tikka Pizza','Supreme Pizza']
Burger=['Zinger Burger','Creamy Mild Burger','Tangy Burger','Chicken Burger']
Roll=['Zinger Roll','Mayo Roll','Max Roll','Chicken Chatni Roll','Chicken Behari Roll']
Fries=['Plain Fries','Garlic Mayo Fries','Pizza Loaded Fries']
Broast=['Chest Broast','Leg Broast','Full Broast']
Barbq=['Chicken Tikka','Malai Boti','Gola kabab','Seekh Kabab','behari Boti']

while True:
    print("\n----------------WELCOME TO CRUST & CRUMS----------------")
    user_input=int(input("Press Accordingly\n1--Order\n0-exit.:\nYour Response: "))
    if user_input==1:
        name=input('Customer Name: ')
        Id=input('Customer ID: ')
        ask=int(input("Order plz!\n1-->Pizza\n2-->Burger\n3-->Roll\n4-->Fries\n5-->Broast\n6-->Barbq  0--> exit\n "))
        if ask==1:
            print("These Pizza Flavours are available!")
            for pizzaitem in pizza:
                print(pizzaitem)
            askm=input("what would you want to buy from above list?   ")
            if askm.title() in pizza:
                print(f'Name: {name}\nID: {Id}')
                print(f'your order for {askm.title()} is Done, Enjoy your meal')
            else:
                print("invalid item, it's not available")
        elif ask==2:
            print("These Burgers are available!")
            for Burgeritem in Burger:
                print(Burgeritem)
            askm=input("what would you want to buy from above list?   ")
            if askm.title() in Burger:
                print(f'Name: {name}\nID: {Id}')
                print(f'your order for {askm.title()} is Done, Enjoy your meal')
            else:
                print("invalid item, it's not available")
        elif ask==3:
            print("These Rolls are available!")
            for Rollsitem in Roll:
                print(Rollsitem)
            askm=input("what would you want to buy from above list?   ")
            if askm.title() in Roll:
                print(f'Name: {name}\nID: {Id}')
                print(f'your order for {askm.title()} is Done, Enjoy your meal')
            else:
                print("invalid item, it's not available")
        elif ask==4:
            print("These Fries Flavours are available!")
            for Friesitem in Fries:
                print(Friesitem)
            askm=input("what would you want to buy from above list?   ")
            if askm.title() in Fries:
                print(f'Name: {name}\nID: {Id}')
                print(f'your order for {askm.title()} is Done, Enjoy your meal')
            else:
                print("invalid item, it's not available")
        elif ask==5:
            print("These Broasts are available!")
            for Broastitem in Broast:
                print(Broastitem)
            askm=input("what would you want to buy from above list?   ")
            if askm.title() in Broast:
                print(f'Name: {name}\nID: {Id}')
                print(f'your order for {askm.title()} is Done, Enjoy your meal')
            else:
                print("invalid item, it's not available")
        elif ask==6:
            print("These Barbq Items are available!")
            for Barbqitem in Barbq:
                print(Barbqitem)
            askm=input("what would you want to buy from above list?   ")
            if askm.title() in Barbq:
                print(f'Name: {name}\nID: {Id}')
                print(f'your order for {askm.title()} is Done, Enjoy your meal')
            else:
                print("invalid item, it's not available")
        elif ask==0:
            print("you don't order any thing!")
    elif user_input==0:
        break
    ask2=input('do you want to continue (y/n): ')
    if ask2!='y':
        print("you are exiting the program!")  
        break
        # user_input=int(input("Press Accordingly\n1--Order\n0-exit.:\nYour Response: "))
    elif ask2=='n':
        print("you are exiting the program!")       

    
    
        
    
