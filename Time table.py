#intrepreter language ?
# --> line by line code (execute)--> byte code --> machine code (slower)
#compiler based language?
#--> can compile whole code @ a time
#high level language
#--> user-->softwre (app) IDE / code editor--> system software (app software: IDE)--> translators--> compiler / intrepreter / assembler --> Hardware (machine language)

#app: software--> compiler/intrepreter --> assembly language (assembler) --> machine code(0,1)
# print("hassi visuals")
#predefined functions 
#frame work-->(library(packages)-->modules)

# input day and it will print it's lectures
lectures={
    'Monday':'DSA || Linear Algebra || Free || Discrete Structures || Free || COAL',
    'Tuesday':'DSA || Linear Algebra || Free || Discrete Structures || Free || COAL',
    'Wednesday':'Free || Linear Algebra || COAL || Discrete Structures || FA || FA',
    'Thursday':'COAL || COAL || COAL || DSA(LAB) || DSA(LAB) || DSA(LAB)',
    'Friday':'COAL || FA || FA',
    'Saturday':'HOLIDAY',
    'Sunday': 'HOLIDAY'
}
flag=True
while flag:
    print("\n------------------------------TIME TABLE 3rd SEMESTER------------------------------")
    inp=int(input("1--> Display whole Time Table\n2--> Individual Day Lectures\n3--> Exit\nType Accordingly: "))
    if inp == 1:
        print("-----Time Table-----")
        for a,b in lectures.items():
            print(a,b)
    elif inp==2:
        ask=input("Type Day: ")

        if ask.title() in lectures.keys():
            print(f'{ask.title()} Lectures are: {lectures[ask.title()]}')
        else:
            print("invalid choice")
    else:
        print("you are exiting the program!")
        flag = False
    


