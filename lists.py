# Print Formatting with Strings

#print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
#print ('')

#name = "Jose"
#print(f'Hello, his name is {name}')
#age = 35
#print(f'Hello, his name is {name} and his age is {age}.')
#num = 0.2193773
#print(f'{num:1.3f}')

my_list = [1,2,3,4,5,6,7,8]

print(my_list)

my_list.append(9) #add to end of list/string

print(my_list)

my_list.pop() #removed last element from list

print(my_list)

my_list.pop(0) #remove element by index

print(my_list)

my_list.remove(3) #remove element by name

print(my_list)

my_list.reverse()

print(my_list)

alphabet = ['a','x', 'd', 'c,']

print(alphabet)

print(alphabet.sort())

new_alphabet = alphabet.sort() #will return None

print(new_alphabet)

alphabet.sort()

new_alphabet = alphabet #will not return None

print(new_alphabet)