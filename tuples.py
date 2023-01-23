# Tuples are very similar to lists. However they have one key difference - immmutability.
# Once an element is inside a tuple, it can not be reassigned. 
# Tuples use parenthesis. i.e. (1,2,3)

t = ['a','a','b']
print(t.count('a'))
print(t.index('a'))

# Tuples have only TWO methods, count() and index().
# Tuples are great for data integrity, as you cannot accidentally reassign. 

b = ([2,3])
print(b)
b[0].append(4)
print(b)