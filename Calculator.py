print("Simple Calculator")
num1= float(input("enter num1 :"))
num2= float(input("enter num2 :"))
operator= input("select operator (+,-,*,/)")
#perform operation
if(operator == "+"):
    result = num1 + num2
elif(operator == "-"):
    result = num1 - num2
elif(operator == "*"):
    result = num1 * num2
elif(operator == "/"):
    if(num2 != 0):
        result = num1 / num2
    else:
        print("not divisible")
else:
    print("enter valid operator")
print("result is: " + str(result))