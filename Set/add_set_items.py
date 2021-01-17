# EX 1
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# Output : {'cherry', 'apple', 'banana', 'orange'}

# EX 2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# Output : {"apple", "banana", "cherry", "pineapple", "mango", "papaya"}