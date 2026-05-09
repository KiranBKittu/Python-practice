sample = set() # {}
# print({'a','b','c'})
sample ={'a', 'b', 'a'}
print(sample)
print(type(sample))
# dictonaries and sets {} same braces but dictonaries are key value pairs set without key value pairs
# sets are unordered collection
#sets removes duplicate values and stores unique values
#print(dir(set))
""" 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update' """

sample.add(10)
print(sample)
#print(sample[0])
# Ordered collection (such as list, tuples, dictionaries) supports indexing
# Unordered collection doesn't supports indexing
s1 = {1,2,3,4}
s2 = {4,6,7,8,1}
print(s1.difference(s2))