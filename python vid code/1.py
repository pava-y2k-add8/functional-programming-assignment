#lists, tuples, sets & dictionary
# int-> whole numbers (no decimal points)
age = 17
print(age)
print(type(age))

print()

#floating point (decimal)
h = 5.8
print(h)
print(type(h))

print()

#string - text/nums - alphanumeric
n = "pava"
print(n)
print(type(n))

print()

#boolean -> 2 values -> true or false
stu = True
print(stu)
print(type(stu))

print("~~~")

age = 17
if age >19:
  print(True)
  print(type(True))
else:
  print(False)
  print(type(False))

print("~~~")

#comparision operators
a = 20 ; b=6
print(a==b)
print(type(a==b))

print()

#type checking
type(h)
type(stu)
type(age)
#if we dont write print, then it will give type for last line
print(type(h))
print(type(stu))
print(type(age))


print()

#type casting (type conversion)
#int -> string
num = 5
r1 = "hello" + str(num)
r2 = "hello" , num
print(r1)
print(type(r1))
print(r2)
print(type(r2))
#also in r2, we cannot use comma we hv to use + cuz we cannot join diff types together

print()

#float <-> int conversion
he = 5.8
print(int(he))
print(float(he))

print()

#string methods -> upper(), lower(), isdigit(), count()
txt = "hello"
new_txt= txt.upper()
print(new_txt)

print()

#operators
#1. Arithmetic -> +, -, /, *, //, %, **
#2. comparision -> ==, !=, >, <, <=, >=
#3. logical -> and, or , not

#arithmetic operators
print(a+b)
print(a-b)
print(a*b)
print(a/b) #normal division -> output always in float
print(a//b) #floor div -> removes decimal point
print(a%b) #provides remainder
print(a**b)

#comparision operators -> output always in boolean
print(a==b)
print(a!=b)

#string comparision (case sensitive)
s1 = "Pava"
s2 = "pava"
print(s1==s2)
print(s1!=s2)

# > & < & <= & =>
x = 45
y =55
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)

per = 18.00
if (per>=18):
  print(True)
else:
  print(False)

#logical operators
x = True
y = False
print(x and y) # if both is true, output is true
print(x or y) # if any one is true, output is true
print(not x) # boolean value reverse

print()

#mini project -> calci
num1 = input("enter 1st num: ")
num2 = input("enter 2nd num: ")
print("Addition = ", num1+num2)
print("Subtraction = ", num1-num2)
print("Multiplication = ", num1*num2)
print("Division = ", num1/num2)
print("Floor division = ", num1 //num2)
print("modulus ", num1%num2) 
print("power/exponent = ", num1**num2)

# control flow
# 1 conditional statements
# 2 if statements
# 3 else statements
# 4 elif statements
# 5 nested conditional statements
# 6 practical exceptcommon error & best practice


print()
#conditional statements -> decision making

#voting eligibility
age = 18
if age>=18:
  print("Eligible for voting")
else:
  print("Not eligible for voting")

age = int(input("enter ur age: "))
if age<13:
  print("u is a child")
elif age<18:
  print("u is a teen")
else:
  print("u is an adult")

print()

#nested conditions
nu = int(input("enter a num: "))
if num>0:
  print("positive")
  if num % 2 == 0:
    print("even")
  else:
    print("odd")
else:
  print("num is zero or negative")

print()

#leap year checker
#1 divisible by 4
#2 divisible by 100 -> not leap yr
#3 divisible by 400 -> leap yr

yr = int(input("enter a yr: "))
if yr % 4 == 0:
  if yr % 100 == 0:
    if yr % 400 == 0:
      print("tis a leap yr")
    else:
      print("tis not a leap yr")
  else:
    print("tis not a leap yr")
else:
  print("tis not a leap yr")


# calc -> if-elif
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Addition =", num1 + num2)
elif operator == "-":
    print("Subtraction =", num1 - num2)
elif operator == "*":
    print("Multiplication =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator")

print()

#ticket pricing

age = int(input("Enter your age: "))
if age > 0 and age <= 100:
    if age < 5:
        print("Free")
    elif age < 12:
        print("₹10")
    elif age < 18:
        is_student = input("Are you a student? (yes/no): ")
        if is_student == "yes":
            print("₹12")
        else:
            print("₹15")
    elif age < 60:
        print("₹50")
    elif age >= 60:
        print("₹10")
else:
    print("Invalid Age")
     