d = {}
d_1 = dict()
# dictionaries are key value pairs and also known as hashmaps
sample = {'a' : 1, 'b' : 2}
print(sample['a'], sample.get('b'))
print(type(sample)) 
# dictonaries and sets {} same braces but dictonaries are key value pairs set without key value pairs

# Dictionaries are Mutable data type
sample['a'] = 10
print(sample)

# we can change values but we can't change keys, Keys in dictionaries, once defined can't be changed
# This should be of immutable datatype for e.g : tuples, string
#print(dir(dict))
print(sample.keys(), sample.values(), sample.items())

sample_list = [(('a','b'),1),('b',2) ]

# type casting
sample_dict = dict(sample_list)
print(sample_dict)