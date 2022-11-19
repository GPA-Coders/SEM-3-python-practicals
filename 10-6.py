name = input("Enter name : ").lower()

value = 0

for i in name:
    value += ord(i) - 96

print("The value is :", value)

# Enter name : python
# The value is : 98