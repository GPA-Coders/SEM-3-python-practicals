f1 = open("11-6-1.txt", "r")
f2 = open("11-6-2.txt", "r")
s1 = f1.read()
s2 = f2.read()
f1.close()
f2.close()

s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")

length = len(s1)

content = ""

for i in range(length):
    content += s1[i] + s2[i]

content += s2[length:]

print("Interleaved string :", content)

# Interleaved string : HSeklyliosWtohrelLdimit