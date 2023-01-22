# Dictionaries are unordered mappings for storing objects. 
# Previously we saw how lists store objects in an ordered sequence.
# Dictionaries use a key-value pairing instead.
# This key-value pair allows users to quickly grab objects without needing to known an idnex location. 
# Dictionaries are unordered and can not be sorted, unlike lists.



d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}} # main syntax of dictionaries are curly braces.

print(d['k1'])
print(d['k2'])
print(d['k2'][2])
print(d['k3']['insideKey'])

e = {'k1':100,'k2':200}
print(e)
e['k3'] = 300
print(e)
e['k1'] = 'NEW VALUE'
print(e)
print(e.keys()) # .keys() returns all the keys.
print(e.values()) # .values() returns all the values.
print(e.items()) # .items() returbs pairings (both keys and values).