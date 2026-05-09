sample = "Hello, How are you doing ??"
#print(sample[0])
#sample[0] = 'h' # it won't works because string are immutable data types
#print(sample)
#print(dir(sample))

""" 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill' """

print(sample.casefold())
#print(sample.center(100,"$"))

""" Interview Questions Like """

# Reverse String 
print(sample[::-1])
# Convert a string as tuple or list
#print(tuple(sample), list(sample))

sample = "Hello, How are you doing ??"

print(sample.split(" ")) # splitting the string
print("#".join(sample.split(" "))) # joining string  and adding * Instead of space

# Concatination : joining two strings
print ("a"+"*"+"b") # a*b