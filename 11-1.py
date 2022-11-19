file = open("11-1.txt", "a")

file.write("This is first line.\n")

line_list = ["This is second line.", "This is third line."]
for line in line_list:
    file.write(line + "\n")

file.close()
file = open("11-1.txt", "r")

print(file.read() + "\n")

lines_read = file.readlines()
for i in lines_read:
    print(i)

lines = len(file.read().split("\n"))
words = len(file.read().split(" "))

print("No. of lines :", lines)
print("No. of words :", words)

file.close()

# This is first line. 
# This is second line.
# This is third line. 

# This is first line.
# This is second line.
# This is third line.

# No. of lines : 3
# No. of words : 12