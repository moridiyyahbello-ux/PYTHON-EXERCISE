# Create an empty tuple
empty_tuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ( 'Anike',  'Nimot')
brothers = ('Adio', 'Ishola', 'Olamiposi')


# join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

#How many siblings do you have?
count_siblings = len(siblings)
print(count_siblings)

#Modify the siblings tuple and 
# add the name of your father and mother and assign it to family_members

parents = ('Oyetunde', 'Abeke')
family_members = parents + siblings
print(family_members)

# Exercises: Level 2
#Unpack siblings and parents from family_member
family_members = ('Oyetunde', 'Abeke', 'Anike', 'Nimot', 'Adio', 'Ishola', 'Olamiposi')
father , mother , *siblings = family_members
parents = (father, mother)
siblings = tuple(siblings)
print(parents)
print(siblings)

# Create fruits, vegetables and animal products 
# tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('Carrot', 'Apple', 'Mango')
vegetables = ('Onion', 'Water leaf', 'Ugwu')
Animal_products = ('Milk', 'Meat', 'Oil')
food_stuff_tp = fruits + vegetables + Animal_products
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = fruits + vegetables + Animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
le_mid = len(food_stuff_lt)
mid_veg = (food_stuff_lt[le_mid // 2])
print(mid_veg)

# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[0:3]
print(first_three)
last_three = food_stuff_lt[-3:]
print(last_three)

#Delete the food_staff_tp tuple completely
# del food_stuff_tp
# print(food_stuff_tp)

#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
check1 = 'Estonia' in nordic_countries
check2 = 'Iceland' in nordic_countries
print(check1)
print(check2)