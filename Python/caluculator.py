


number_1 = int(input("Enter number 1:"))
number_2 = int(input("Enter number 2:"))

operation = input("Now choose operation: +,-,* or /: ")
result = None
if operation == "+":
    print("Addition: "+ str(number_1 + number_2))
elif operation == "-":
    print("Substraction: " + str(number_1 - number_2 ))
elif  operation == "*":
    print("Multiplication:" +str(number_1 * number_2))
elif operation == "/":
    print("Division: " + str(number_1 / number_2) )

