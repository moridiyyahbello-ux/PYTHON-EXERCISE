# Exercises: Level 1
# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:

# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

# get_user = int(input("Enter your age: "))
# if get_user >= 18:
#     print("You are old enough to learn to drive.")
# else:
#     print(f"You need {18 - get_user} more years to learn to drive.")

# '''
# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' 
# for bigger differences, and a custom text if my_age = your_age. Output:

# Enter your age: 30
# You are 5 years older than me.
# '''

# my_age = 25
# your_age = int(input("Enter your age: "))
# if your_age > my_age:
#     age_diff = your_age - my_age
#     if age_diff == 1:
#         print("You are 1 year older than me.")
#     else:
#         print(f"You are {age_diff} years older than me.")
# elif your_age < my_age:
#     age_diff = my_age - your_age
#     if age_diff == 1:
#         print("I am 1 year older than you.")
#     else:
#         print(f"I am {age_diff} years older than you.")
# else:
#     print("We are the same age.")
    
# '''
# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, 
# else a is equal to b. Output:

# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# '''
# a = int(input('Enter number one: '))
# b = int(input('Enter number two:'))

# if a > b:
#     print(f"{a} is greater than {b}")
# elif a < b:
#     print(f"{a} is smaller than {b}")
# else:
#     print(f"{a} is equal to {b}")

# #Write a code which gives grade to students according to theirs scores:
# '''
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
# '''

# get_score = int(input("Enter your score: "))
# if 80 <= get_score <= 100:
#     print("Your grade is A.")
# elif 70 <= get_score <= 79:
#     print("Your grade is B.")
# elif 60 <= get_score <= 69:
#     print("Your grade is C.")
# elif 50 <= get_score <= 59:
#     print("Your grade is D.")
# elif 0 <= get_score <= 49:
#     print("Your grade is F.")

# Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter. March, April or May, 
# the season is Spring June, July or August, the season is Summer

# get_season = input('Enter Month here: ')

# if get_season == 'September' or get_season == 'October' or get_season == 'November':
#     print('The season is Autumn')
# elif get_season == 'December' or get_season == 'January' or get_season == 'February':
#     print('The season is Winter')
# elif get_season == 'March' or get_season == 'April' or get_season == 'May':
#     print('The season is Spring')
# elif get_season == 'June' or get_season == 'July' or get_season == 'August':
#     print('The season is Summer')

# # The following list contains some fruits:


# '''If a fruit doesn't exist in the list add the fruit to the list
# and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
# '''
# fruits = ['banana', 'orange', 'mango', 'lemon']
# get_fruit = input('Enter fruit here: ')
# if get_fruit in fruits:
#         print('That fruit already exist in the list')
# else:
#         fruits.append(get_fruit)
#         print(fruits)

# Exercises: Level 3

'''
Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), 
 if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
    Asabeneh Yetayeh lives in Finland. He is married.
'''

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    middle_skill = len(person['skills']) // 2
    print(list(person['skills'])[middle_skill])
if 'skills' in person:
    if 'Python' in person['skills']:
        print('Python was found')
if 'skills' in person:
    skills = person['skills']
if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print('He is a front end developer')
if 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
else:
        print('unknown title')
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
        

