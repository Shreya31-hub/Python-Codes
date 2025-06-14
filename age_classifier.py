print("age classifier")
Name = input("enter your name")
age = int(input("enter age"))
print("Hello " +Name)
if(age<=12):
    print("You are Child")
elif(age<=19):
    print("You are Teenager")
elif(age<=60):
    print("You are adult")
elif(age>60):
    print("YOu are Senior Citizen")
else:
    print("enter valid number")