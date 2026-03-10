#hotel short management system
#two classes: Account : Staff
#object Oriented programming
#here we have to create account, than login it and our focus is to check the Employee Dashboard where names, id's,job status and timing are shown:

#---------------------------------- Happy To See What I have Made ------------------------------
class Account:
    def __init__(self):
        pass
    def createAccount(self):
        name=input("Enter a FullName: ")
        username=input("Enter a Username: ")
        userpassword=input("Enter a Password: ")
        usergender=input(f"Enter a Gender: Male\Female: ")
        print(f'Loading......\n-----------Account Successfully Login---------')

    def login(self):
        username=input("Enter a Username: ")
        userpassword=input("Enter a Password: ")

    
class Staff:
    
    def employee_details(self):
        self.names=["Haseeb","Aleem","Saim","Hadiyan"]
        self.ID=[123,345,657,890]
        self.Job=["cook","Boss","Receptionist","waiter"]
    
    def employee_timing(self):
    #    self.boss="9:00 - 9:00"
    #    self.cook="9:00 - 12:00"
    #    self.receptionist="11:00 - 12:00"
    #    self.waiter="11:00 - 9:00"
        self.timing=["9:00 - 12:00","9:00 - 9:00","11:00 - 12:00","11:00 - 9:00"]
    
#--------------objects------------------

emp=Staff()
obj=Account()
user=int(input("Your Choice Plz: \npress--> 1 for creating Acccount: \npress--> -1 for Login Account: \npress--> 0 for Exiting: \nChoice pressed: "))
while(user!=0):
    if user==1:
        obj.createAccount()
    elif user==-1:
        obj.login()
        print("---------------- Employee DashBoard -------------------")
        us=int(input("Employee Details: \nEmployee Name: 1\nEmployee ID: 2\nEmployee JOB: 3\nEmployee info complete: 4\nEmployee info complete with Timig: 5\nExiting---> 0\nPressed choice: "))
        
        while(us!=0):
            if us==1:
                emp.employee_details()
                print(f'Employee Names: {emp.names}')
            elif us==2:
                emp.employee_details()
                print(f'Employee ID"s: {emp.ID}')
            elif us==3:
                emp.employee_details()
                print(f'The Employee Job status: {emp.Job}')
            elif us==4:

                emp.employee_details()
                emp.employee_timing()
                print(f'--------- All Employee Record ----------')
                print(f'Employee Names: ')
                for i in emp.names:
                    print(" ",i)
                print(f'Employee ID: ')
                for j in emp.ID:
                    print(" ",j)
                print(f'Employee Job status: ')
                for k in emp.Job:
                    print(" ",k)
                
            elif us==5:
                emp.employee_timing()
                emp.employee_details()
                print(f'----------Employee Data---------')
                for i in range(0,4):
                    print(f"Name: {emp.names[i]} || ID: {emp.ID[i]} || Job: {emp.Job[i]} || Timing: {emp.timing[i]} \n")
            print(f'\n\t\t------------------------------------------------')
            if us==0:
                break
            us=int(input("Employee Details: \nEmployee Name: 1\nEmployee ID: 2\nEmployee JOB: 3\nEmployee info complete: 4\nEmployee info complete with Timig: 5\nExiting---> 0\nPressed choice: "))
        print("----------- Exiting Employee DashBoard ---------------") 
    elif user==0:
        print(f'----------- The Program is Exiting --------------')
        raise SystemExit
    else:
        print("Invalid Choice entered")
    print(f'\n\t\t------------------------------------------------')
    user=int(input("Your Choice Plz: \npress--> 1 for creating Acccount: \npress--> -1 for Login Account: \npress--> 0 for Exiting: \nChoice pressed: "))
    
    

        

    
    
    

