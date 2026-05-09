# LOOPS are of two type --> for , while
value = 0
""" while value < 10:
    print(value)
    value = value+1 """
# break
""" while value < 10:
    if value == 5:
        break
    print(value)
    value = value+1 """

# continue
""" while value < 10:
    if value == 5:
        # Incrementing is very important
        #value = value + 1 or same as value += 1 
        value += 1
        continue
    print(value)
    value = value+1 """
samples = ["server1", "server2", "server3", "server4"]
""" idx = 0
while idx < len(samples):
    print(samples[idx])
    idx +=1 """
############ FOR ##########
# -> in == > membership operator (checks whether that element is present or not)
#print(1 in samples) # IT check 1 is present in samples list, if not present it returns false

# access element inside a list with index using for loop
# range, enumerate

# element is iterable
# sample is iterator

""" for element in samples:
    print(element) """

print(list(range(5)))

for idx in range(len(samples)):
 print(samples[idx])
 
""" # enumerate is useful for obtaining an indexed list: """
for val in enumerate(samples):
 print(val)

for val, server in enumerate(samples):
 print(val, server)

#tuple unpacking
a, b = (1, 2)
print(a, b)