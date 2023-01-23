# Sets are unordered collections of UNIQUE elements.
# Meaning, there can only be one representative of the same object.

myset = set()
print(myset) # This is an empty set.
myset.add(1) # add() method adds an element instead of appened()
print(myset) # The element '1' was added. Notice, curly braces makes it look like a dictionary but there no key-value pairs.
myset.add(2) 
print(myset) 
myset.add(2)
print(myset) # Notice '2' was added as it already exists. 

# Sets are useful to remove repeated elements. i.e.

mylist = [2,2,1,1,1,1,1,3,3,3,3,3]
print(mylist)

newset = set(mylist)
print(newset) # Be aware, it may look like it's been ordered but it's not. As shown below. 

mylist2 = ['b','b','a','a','a','c','c','c']
print(mylist)

newset2 = set(mylist2)
print(newset2)