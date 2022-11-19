file1 = open("11-4-1.txt", "r")
content = file1.read()
file1.close()

content = content.split(" ")

for word in content:
    if len(word) == 4:
        content[content.index(word)] = "****"

content = " ".join(content)

file2 = open("11-4-2.txt", "w")
file2.write(content)
file2.close()