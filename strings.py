#EXERCISE DAY 4
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Coc = ['Thirty', 'Days', 'Of', 'Python']
res = ' '.join(Coc)
print(res)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
conc = ['Coding', 'For' , 'All']
resu = ' '.join(conc)
print(resu)

#Declare a variable named company and assign it to an initial value "Coding For All".
#Print the variable company using print().
#Print the length of the company string using len() method and print().
#Change all the characters to uppercase letters using upper() method.

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
cut_slice = company.split()
print(cut_slice[0])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))
# Change Python for Everyone to Python for All using the replace method or other methods.
rCompany = 'Python for Everyone'
print(rCompany.replace('Python for Everyone', 'Python for All'))
# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))
# What is the character at index 0 in the string Coding For All.
print(company[0])
# What is the last index of the string Coding For All.
print(len(company) - 1)
# What character is at index 10 in "Coding For All" string.
print(company[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
acr = 'Python For Everyone'
sp_acr = acr.split()
find_index = [sp_acr[0][0], sp_acr[1][0], sp_acr[2][0]]
print(''.join(find_index))
# Create an acronym or an abbreviation for the name 'Coding For All'.
acro = 'Coding For All'
sp_acro = acro.split()
find_index = [sp_acro[0][0], sp_acro[1][0], sp_acro[2][0]]
print(''.join(find_index))
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find('because'):sentence.rfind('because')+len('because')])
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[sentence.find('because'):sentence.rfind('because')+len('because')])

# Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))
# Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
small_coding = '   Coding For All      '
print(small_coding.strip())

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

identifier1 = '30DaysOfPython'
identifier2 = 'thirty_days_of_python'
print(identifier1.isidentifier())
print(identifier2.isidentifier())
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
py_libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(py_libs))
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
sep_sentences = "I am enjoying this challenge.\nI just wonder what is next."
print(sep_sentences)
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
lines = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(lines)
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

num1 = 8
num2 = 6
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
