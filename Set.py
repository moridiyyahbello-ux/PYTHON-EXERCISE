#Exercises: Level 1

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
find_lent = len(it_companies)
print(find_lent)

# Add 'Twitter' to it_companies

it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies

it_companies.update(['MTN','AIRTEL', 'GLO'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('GLO')
print(it_companies)

#What is the difference between remove and discard
'''
remove() will raise an error if the item to be removed is not found
discard() will not raise error 
'''
# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
D = A.intersection(B)
print(D)

# Is A subset of B
E = A.issubset(B)
print(E) #True

# Are A and B disjoint sets
F = A.isdisjoint(B)
print(F) #False

# Join A with B and B with A
G = B.union(A)
H = C.union(A)
print(H)

# What is the symmetric difference between A and B
I = A.symmetric_difference(B)
print(I)

# Delete the sets completely
del A
del B
# print(A)
# print(B)

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages_list = set(age)
compare_lists = len(age) > len(ages_list)
compare_lists_2 = len(age) < len(ages_list)
compare_lists_3 = len(age) == len(ages_list)
print(ages_list)
print(compare_lists)
print(compare_lists_2)
print(compare_lists_3)

# Explain the difference between the following data types: string, list, tuple and set

# I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.

words = 'I am a teacher and I love to inspire and teach people'
spl_words = words.split()
print(spl_words) #['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people']
s_words = set(spl_words)
print(s_words) #{'people', 'teacher', 'am', 'inspire', 'I', 'a', 'teach', 'and', 'to', 'love'}
print(len(s_words)) #10 unique words

