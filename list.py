#Lists 
#Declare an empty list
empty_list = []

#Declare a list with more than 5 items
lst_5 = ['Cat', 'Dog', 'Cow', 'Rat', 'Kitten']
print(lst_5)

#Find the length of your list
print(len(lst_5))

#Get the first item, the middle item and the last item of the list
first_item = lst_5[0]
middle_item = lst_5[len(lst_5)//2]
last_item = lst_5[-1]
print( first_item)
print(middle_item)
print(last_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['Bello Moridyyah', 32, 5.5, 'Single', '32 Colony street']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
first_com = it_companies[0]
mid_com = it_companies[len(it_companies)//2]
last_com = it_companies[len(it_companies)- 1]
print(first_com)
print(mid_com)
print(last_com)

# Print the list after modifying one of the companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[1] = 'FireFox'
print(it_companies)

#Add an IT company to it_companies
it_companies.append('Google')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Twitter')
print(it_companies)

#  Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
join_companies = '#;  '.join(it_companies)
print(join_companies)

# Check if a certain company exists in the it_companies list.
com_check = 'Google' in it_companies
print(com_check)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_3 = it_companies[:3]
print(first_3)

# Slice out the last 3 companies from the list
last_3 = it_companies[-3:]
print(last_3)

# Slice out the middle IT company or companies from the list
middle_com = it_companies[len(it_companies)//2:len(it_companies)//2 + 1]
print(middle_com)

# Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies)

# Remove the middle IT company or companies from the list
middle_it = len(it_companies) // 2
it_companies.remove(it_companies[middle_it])
print(it_companies)

# Remove the last IT company from the list
it_companies.remove(it_companies[-1])
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
# del it_companies
# print(it_companies)

# Join the following lists:

# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 26. 
# Copy the joined list and assign it to a variable full_stack, 
# then insert Python and SQL after Redux.

full_stack = front_end + back_end
full_stack.insert(4, 'Python')
full_stack.insert(4, 'SQL')
print(full_stack)

# Exercises: Level 2

#Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = min(ages)
max_age = max(ages)
print(min_age)
print(max_age)

# Find the median age (one middle item or two middle items divided by two)
median_age_1 = ages[len(ages) // 2]
median_age_2 = ages[len(ages) // 2 -1]
median = int((median_age_1 + median_age_2) / 2)
print(median_age_1)
print(median_age_2)
print(median)

# Find the average age (sum of all items divided by their number)
average_age = sum(ages) / len(ages)
print(int(average_age))

# Find the range of the ages (max minus min)
range_age = max_age - min_age
print(range_age)

# Compare the value of (min - average) and (max - average), use abs() method
compare_min = abs(min_age - average_age)
compare_max = abs(max_age - average_age)
com_abs = (compare_min < compare_min)
print(com_abs)
print(int(compare_min))
print(int(compare_max))

#Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
count_countries = len(countries)
print(count_countries)
middle_countries = countries[count_countries // 2]
print(middle_countries)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
middle = len(countries) // 2 + len(countries) % 2
country_one = countries[:middle]
country_two = countries[middle:]
print(country_one)
print(country_two)

# ['China','Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
new_countries = ['China','Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
one, two, three, *scandic_rest = new_countries
print(new_countries)