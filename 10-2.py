s = input("Enter string : ").lower()

tup = (0, 0)

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        ntup = (tup[0]+1, tup[1])
        tup = ntup
    else:
        ntup = (tup[0], tup[1]+1)
        tup = ntup

print("Vowels :", tup[0])
print("Consonants :", tup[1])

# Enter string : PyThOn
# Vowels : 1
# Consonants : 5