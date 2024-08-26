# PYTHON PROGRAM

# NAME
name=input("Enter your name:")

#FOR LOOP(TABLE)
tab = int(input("what is the no. of table."))
num = int(input("How many times of table run"))

for i in range(1,num+1):
    print(tab , "x" , i , "=" , tab*i)
print("This is your table",tab, "and it run" ,i,"times")
print("Your table has been completed")

#FOR LOOP(TABLE)
tab = int(input("what is the no. of table."))
num = int(input("How many times of table run"))

for i in range(1,num+1,2):
    print(tab , "x" , i , "=" , tab*i)
print("This is your table",tab, "and it run" ,i,"times")
print("Your table has been completed")

#FOR LOOP(TABLE)
tab = int(input("what is the no. of table."))
num = int(input("How many times of table run"))

for i in range(2,num+1,2):
    print(tab , "x" , i , "=" , tab*i)
print("This is your table",tab, "and it run" ,i,"times")
print("Your table has been completed")

# MAKING MARK SHEET

#NAME
name=input("Enter Your name:")

#CALCULATION
eng=int(input("Enter eng. marks:"))
tajv=int(input("Enter tajveed. marks:"))
math=int(input("Enter math. marks:"))
sci=int(input("Enter sci marks:"))
com=int(input("Enter comp. marks:"))

obtain=(eng+tajv+math+sci+com)
per=(obtain/275*100)

print("your obtain marks are:",(obtain))
print("your percentage is:",(per))

#FINDING GRADE
if per > 70 and per < 100:
    grade="A1"
elif per >60 and per < 70:
    grade="A"
elif per > 40 and per <60:
    grade="B"
else:
    grade="fail"
    
print(f"your rank is: {grade}")
print("sir my project has been completed")
    # TODO: write code...