#Level three
# Age = 32
# height = 5.5
# complex_number = 1 + 2j
# print(complex_number)

# Enter_base = input("Enter base: ")
# Enter_height = input("Enter height: ")
# MY_base = int(Enter_base)
# My_height = int(Enter_height)
# Area = int(0.5 * MY_base * My_height)
# print("The area of the triangle is:", Area) 

# #  Question 4
# Enter_side_A = input("Enter side a: ")
# Enter_side_B = input("Enter side b: ")
# Enter_side_C = input("Enter side c: ")

# SideA = int(Enter_side_A)
# SideB = int(Enter_side_B)
# SideC = int(Enter_side_C)
# Perimeter = SideA + SideB + SideC
# print("The perimeter of the triangle is:", Perimeter)

# #  Question 6
# length = int(input("Enter Length: "))
# width = int(input("Enter Width: "))
# Area = length * width
# Perimeter = 2 * (length + width)
# print("The area of the rectangle is:", Area)
# print("The perimeter of the rectangle is:", Perimeter)


# # Question 7: Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# radius = int(input("Enter Radius: "))
# pi = float(3.14)
# area = int(pi * radius * radius)
# circumference = int(2 * pi * radius)
# print("The area is:", area)
# print("The circumference:", circumference)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
n = 2
m = -2
x_intercept = -m / n
y_intercept = m
print("The slope is:", n)
print("The x-intercept is:", x_intercept)
print("The y-intercept is:", y_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
slope = (y2 - y1) / (x2 - x1)
Euc_distance = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
print("The slope is:", slope)
print("The Euclidean distance is:", Euc_distance)

#Compare the slopes in tasks 8 and 9.
slope1 = 2
slope2 = slope
x = slope1 > slope2
y = slope1 < slope2
print(x)
print(y)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

X = -3
Y = X**2 + 6*X + 9
print(int(Y))

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

str1 = len('python')
str2 = len('dragon')
M = str1 > str2
print(M)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
check1 = 'python' 
check2 = 'dragon'
print(check1.find('on') and check2.find('on'))

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
words = 'I hope this course is not full of jargon.'
print('jargon' in words) 

#There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

#Find the length of the text python and convert the value to float and convert it to string
find = len('python')
float_val = float(find)
string_val = str(float_val)
print(float_val)
print(string_val)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input('Enter a number:'))
even = num % 2 == 0
print(even)

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

floor_div = 7 // 3
num = int(2.7)
print(floor_div == num)

#Check if type of '10' is equal to type of 10
ty1 = '10'
ty2 = 10
print(type(ty1) == type(ty2))

#Check if int('9.8') is equal to 10
num1 = int(float('9.8'))
num2 = 10
print(num1 == num2)

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hrs = int(input('Enter hours:')) 
rate = int(input('Enter rate per hour:'))
pay = int(hrs * rate)
print('Your earning is:', pay)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter number of years: '))
total_sec = int(years * 366 * 24 * 60 * 60)
print(f'You have lived for {total_sec} seconds')

#Write a Python script that displays the following table
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64') 
print('5 1 5 25 125')

