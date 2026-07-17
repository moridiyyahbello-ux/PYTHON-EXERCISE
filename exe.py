# Acess the second item in the third list

#Access the second item in the third list
# dict_items = [['key1', 'value1'], 
#               ['key2', 'value2'], 
#               ['key3', 'mango'], 
#               ['key4', 'value4']]
# a = dict_items[2][1]
# print(a)

# is_hungry = False
# if is_hungry:
#     print('Action')
# else:
#     print('I am Hungry')
    
# age = 17
# if age < 18:
#     print('Underage')
# elif 18 >= age <= 30:
#     print('MiddleAge')
# else:
#     print('OverAge')
    

'''
a = input("Enter a value: ")
b = input("Enter b value: ")
swap = a
a = b
b = swap
print(a,b)
'''

'''
en_ter = ((input("Enter two digit number: ")))
one = en_ter[0] 
two = en_ter[1]
add = int(one) + int(two)
print(int(add))
'''

name_int = int(input("Enter two number and get lucky name: "))
cov = str(name_int)
one_name = str(cov[0])
two_name = str(cov[1])

if cov[0] == '1':
    print(one_name + two_name)


    