print("Hello and welcome to my python calculator!")

def add (x,y): #addition operation function
  return x + y
def subtract (x,y): #subtraction operation function
  return x - y
def multiply (x,y): #multiplication operation function
  return x*y
def divide (x,y): #division operation function
  return x/y
def remainder (x,y): #remainder operation function
  return x%y
def exponent (x,y): #exponent operation function
  return x**y
def compare(x,y): #comparing two numbers function
  if x==y:
    return ("true")
  else:
    return ("false")
def greater (x,y):
  if x > y:
    return (str(x) + " is greater than " + str(y))
  else:
    return(str(y) + " is greater than " + str(x))

print("") #prints blank space
print("Select operation: ") 
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
print("5. remainder")
print("6. exponent")
print("7. are these two numbers equal?")
print("8. which number is greater?")

print("") #prints blank space
choice = input("Enter choice(1/2/3/4/5/6/7/8):")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if choice == '1':
 print (num1, "+",num2,"=", add(num1,num2)) #calls add function

elif choice == '2':
  print(num1,"-",num2,"=", subtract(num1,num2)) #calls subtract function

elif choice == '3':
  print(num1,"*",num2,"=", multiply(num1,num2)) #calls multiply function

elif choice == '4':
  print(num1,"/",num2,"=", divide(num1,num2)) #calls divide function

elif choice == '5':
  print(num1,"%",num2,"=", remainder(num1,num2)) #calls remainder function
elif choice == '6':
  print(num1, "**",num2, "=", exponent(num1,num2))
elif choice == '7':
  print(num1,"==", num2, compare(num1,num2))
elif choice == '8':
  print(num1,"and", num2, greater (num1,num2) )
else:
  print("Invalid input.  Press the run buttom to try again")

print("") #prints blank space
print("Thanks for using my python calculator! Click the run buttom to use it again!")
