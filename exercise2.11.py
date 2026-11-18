number = int(input('Enter a five digit number: '))
number1 = number//10000
number = number % 10000
number2 = number//1000
number = number % 1000
number3 = number//100
number = number % 100
number4 = number//10
number = number % 10
print (f"{number1}   {number2}   {number3}   {number4}   {number}")