# ways to specify the list
l = [] 
l1 = list()
# ways to specify the tuples
t = ()
t1 = tuple()

samples = ("172.19.30.90","172.19.30.91",True, 123, 138.00)
#print(type(samples))

# Tuple is immutable
#samples[0] = 12 # we can't modify tupples we get error if we do this
#print(samples)

print(samples[0:2]) # we can use slicing in tuples also.
print(samples[-1]) # we can use negitive indexing also.

# when ever we planned to not to change the elements then we can go for tuples.

env = ("DEV", "PREPROD", "TEST", "DR", "PROD")
print(type(env))

#print(dir(tuple))
# 'count', 'index'

s1 = (1,2,3,4,5,5,6,7)
print(s1.count(5), s1.count(10))
print(s1.index(5))

# Type casting : Datatype consvertion 

# tuple to list conversion
samples = ("172.19.30.90","172.19.30.91",True, 123, 138.00)
s2 = list(samples)
print(type(s2), s2)

# list to tuple conversion
s3 = tuple(s2)
print(type(s3), s3)