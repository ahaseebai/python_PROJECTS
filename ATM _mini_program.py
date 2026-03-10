flag=True
while flag:
    user_input=int(input("Balance:"))
    options=input("display options to    withdraw   ||    deposit   ||     checkbalance: ")
    if options == 'withdraw':
        print(f'your balance is: {user_input} and it is Successfully withdrawn')
    elif options == 'deposit':
        print(f'your balance is: {user_input} and new amount will be deposited!')
    elif options == 'checkbalance':
        print(f'your balance is: {user_input} ')
    another_input=input("do you want to continue (yes/no): ")
    if another_input =='no':
        flag=False

        
    
