# Exercises: Day 8
#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary

dog = {
    'name' : 'rex',
    'color' : 'brown',
    'breed' : 'german shepherd',
    'legs' : 4,
    'age' : 3
}
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Moridiyyah',
    'last_name' : 'Bello',
    'gender' : 'Female',
    'age' : 20,
    'marital_status' : 'Single',
    'skills' : ['Python', 'HTML', 'CSS'],
    'country' : 'Nigeria',
    'city' : 'Lagos',
    'address' : '32 Colony street'
}

# Get the length of the student dictionary
print(len(student))

# Modify the skills values by adding one or two skills
student['skills'].append('JavaScript')
student['skills'].append('React') 
print(student['skills'])

# Get the dictionary keys as a list
keys_list = list(student.keys())
print(keys_list)

# Get the dictionary values as a list
values_list = list(student.values())
print(values_list)

# Change the dictionary to a list of tuples using items() method
student_list = list(student.items())
print(student_list)

# Delete one of the items in the dictionary
del student['marital_status']
print(student)
#Delete one of the dictionaries
del student


