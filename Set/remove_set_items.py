# EX 1
thislset = {"apple", "banana", "cherry"}
thislset.remove("banana")
print(thislset) # Output : {'apple', 'cherry'}

# EX 2
thislset = {"apple", "banana", "cherry"}
thislset.discard("banana")
print(thislset) # Output : {'cherry', 'apple'}

# EX 3
thislset = {"apple", "banana", "cherry"}
x = thislset.pop()
print(thislset) # Output : {'cherry', 'banana'}


# EX 4
thislset = {"apple", "banana", "cherry"}
thislset.clear()
print(thislset) # Output : set()