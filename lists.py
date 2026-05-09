server_1 = "172.19.30.90"
server_2 = "172.19.30.91"
 # instead of giving 100's of ip addresses we can give as a list like below using []
servers = ["172.19.30.90","172.19.30.91",True, 123, 138.00]
print(type(servers))
print(type(servers), servers, server_1, server_2)

# to get a server from list of server we can give from list of index by default index will start from 0
# Python is zero indexed based.
server_1 = servers[1]
print("Server 1 IP address is :",server_1) # we can use string also in double codes with comma separation
#========================= Slicing =================================
# Slicing (start_index:end_index), as end_index in python in inclusive
simple_slicing = servers[1:4]
print("This are indexes", simple_slicing)
simple_slicing = servers[1:]
print("This are indexes after 1", simple_slicing)
simple_slicing = servers[:4]
print("This are slicing index from starting to 4 indexed",simple_slicing)
simple_slicing = servers[:]
print("This are slicing index to get all",simple_slicing)

""" text = "Python"

print(text[1:4])
output : yth
P  y  t  h  o  n
0  1  2  3  4  5

Slice [1:4] means:
Start from index 1 ✅ (y)
Stop before index 4 ❌ (o not included)
So included indexes are: 1, 2, 3 """
#========================= Step Size=================================
#step size
text = "Python"
print("This is step size how many steps it should is 2 : ",text[0:6:2])

""" start → where to begin
end → stop before this index
step → how many positions to move each time 
it takes 0, 2, 4 """
#====================== Negitive Indexing ====================================
# Negative indexing means counting from the end of the string/list.
text = "Python"
print(text[-1])

"""  
P   y   t   h   o   n
-6  -5  -4  -3  -2  -1 """
#======================= Length of Indexing ===================================
print(len(text)) # to get length of the string
#====================== Replace ====================================
# List is a mutable datatype
# Immutable: once defined it can't be changed eg: tuples, sets
print("Before modify:", servers)

# Mutable: once defined it can be changed eg: list, dictonaries
servers[-3] = 1234 # Mutable datatype we changing -3 data type as 1234 as it is before 123 or Inplace operation
print("After modification:", servers)
#==========================================================
#print("List of Operations:", dir(servers)) # What type of operations we can perform we can check it

""" ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']] """

#====================== Append ====================================
print("Before:", servers)
servers.append(False)
servers.append(["a","b"])
print("After Appending:", servers, len(servers))
print(servers[-1][0])
print(servers[-1][1])
""" append()
Adds one single element to the end of the list.
That element can be anything (even another list).
lst = [1, 2, 3]
lst.append([4, 5])
print(lst)
[1, 2, 3, [4, 5]]
👉 Notice: the list [4, 5] is added as a single nested element. """
# Multi Indexing

#========================== Extend & Length of string ================================
servers.extend(["c","d"])
print("After extend :", servers, len(servers))
""" extend()
Adds each element from an iterable (like a list, tuple, string) to the list.
It “unpacks” the iterable and adds items individually.
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)
[1, 2, 3, 4, 5]
👉 Here, 4 and 5 are added as separate elements. """
#=========================== To check index location ===============================
servers = ["172.19.30.90","172.19.30.91",True, 123, 138.00]

print(servers.index(True)) # To check the index number of True
#====================== Insert ====================================
servers.insert(3,12) # To insert 12 at 3 index value
print(servers)
#========================= Remove =================================
servers.remove(True)
print(servers)
#========================= Reversing =================================
servers.reverse()
print(servers)
#======================= Reverse Listing ===================================
servers = ["app1", "app2", "app3"]

print(servers[::-1]) # in Python is used to reverse a list (or string, tuple, etc.).

""" In [::-1]:

start → empty → start from beginning
end → empty → go till end
step → -1 → move backwards one step """
#========================= sort & sorted =================================
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)
new_list = sorted(numbers)
print(new_list)
print(sorted(numbers, reverse=True))

""" "Here sort() changed the original list itself."
"sorted() created a new sorted list and kept the original list unchanged." """
#========================= Remove & Copy =================================
servers = ["172.19.30.90","172.19.30.91",True, 123, 138.00]
servers_1 = servers.copy()
print(servers_1)
servers_1.remove(True)
print(servers, servers_1)

""" Interview Questions

1. Reverse a list
2. sort vs sorted
3. Integer division vs float division
4. Shallow copy (Inplace operation)
5. Multi indexing
6. append vs extend
7. Mutable vs immutable
8. dir() """