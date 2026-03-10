# write a program to make a marksheet, program should ask 
# name,class,roll number,obtained marks,and give you percentage as well as grade:

print("--------------------- MARKSHEET ---------------------------")
name=input("Type your name: ")
roll_no=int(input("Type your roll number: "))
department=input("Type your department: ")
obt_marks=int(input("Type your obtained marks: "))
total_marks=int(input("Type your total marks: "))
percent=float(obt_marks*100)/total_marks
if percent>=90:
    grade='A+'
elif percent>=80:
    grade='A-1'
elif percent>=70:
    grade='A'
elif percent>=60:
    grade='B'
elif percent>=50:
    grade='C'
elif percent>=40:
    grade='D'
else:
    grade='you are failled Better Luck Next Time!'
print(f'name: {name}\nRoll numner: {roll_no}\nDepartment: {department}\nObtained Marks: {obt_marks}\nTotal Marks: {total_marks}\nPercentage: {percent}\nGrade: {grade}')


