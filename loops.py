#Exercises: Level 1
from data.countries_data import countries_data
#Iterate 0 to 10 using for loop, do the same using while loop.
# for i in range(11):
#     print(i)

# i = 0
# while i <= 10:
#     print(i)
#     i += 1
# # Iterate 10 to 0 using for loop, do the same using while loop.

# for i in range(10,-1):
#     print(i)

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

# # Write a loop that makes seven calls to print(), 
# # so we get on the output the following triangle:
# # '''
# #   #
# #   ##
# #   ###
# #   ####
# #   #####
# #   ######
# #   #######
# # '''

# for i in range(1,8):
#     print("#"*i)
    
# #Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

# counter = 0
# for i in range(8):
#     for k in range(8):
#         print("#", end=" ")
#     print()
    
# # Print the following pattern:

# # 0 x 0 = 0
# # 1 x 1 = 1
# # 2 x 2 = 4
# # 3 x 3 = 9
# # 4 x 4 = 16
# # 5 x 5 = 25
# # 6 x 6 = 36
# # 7 x 7 = 49
# # 8 x 8 = 64
# # 9 x 9 = 81
# # 10 x 10 = 100

# # for i in range(11):
# #     print(f"{i} x {i} = {i*i}")

# # Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# new_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
# for item in new_list:
#     print(item)

# # Use for loop to iterate from 0 to 100 and print only even numbers
# # for i in range(0,100,2):
# #     print(i)
    
# # Use for loop to iterate from 0 to 100 and print only odd numbers
# # for k in range(1,100,2):
# #     print(k)
    
# # Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# # The sum of all numbers is 5050.
# # add = 100
# # for i in range(101):   
# #     add += i
# #     print(f"The sum of all numbers is {add}")
# #Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# # add_even = 0
# # add_odd = 0
# # for i in range(0,101,2):
# #     add_even += i
# # for i in range(1,101,2):
# #     add_odd += i
# # print(f"The sum of all evens is {add_even}")
# # print(f"The sum of all odds is {add_odd}")

# # Go to the data folder and use the countries.py file. 
# # Loop through the countries and extract all the countries containing the word land.

# countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cabo Verde','Cambodia','Cameroon','Canada','Central African Republic','Chad','Chile','China','Colombia','Comoros','Congo, Democratic Republic of the','Congo, Republic of the','Costa Rica',"Côte d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor-Leste)','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Eswatini','Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Macedonia','Norway','Oman','Pakistan','Palau','Palestine','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe'
# ]
# i = 'land'
# store_countries = []
# for country in countries:
#     if i in country:
#         store_countries.append(country)
# print(store_countries)

# # This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# fruits_lst = ['banana', 'orange', 'mango', 'lemon']
# store_fruits = []
# for i in fruits_lst[::-1]:
#     store_fruits.append(i)
# print(store_fruits)

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
store_lang = []

for c in countries_data:
    for language in c ['languages']:
            store_lang.append(language)
    count = len(store_lang)  
print(int(count))
# Find the ten most spoken languages from the data
lang_store = {}
for country in countries_data:
    for language in country['languages']:
        if language in lang_store:
            lang_store[language] += 1
        else:
            lang_store[language] = 1
sorted_lang = sorted(lang_store.items(), key=lambda item: item[1])[::-1][:10]
for item in sorted_lang:
    print(item[0])
# Find the 10 most populated countries in the world

populated_countries = []
for country in countries_data:
    populated_countries.append((country['name'], country['population']))

sorted_populated = sorted(populated_countries, key=lambda item: item[1]) [::-1][:10]
for item in sorted_lang:
    print(item[0])