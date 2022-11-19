s1 = input("Enter first word : ")
s2 = input("Enter second word : ")

w1 = list(s1).sort()
w2 = list(s2).sort()

if w1 == w2:
    print("The words are anagrams")
else:
    print("the wrods are not anagrams")

# Enter first word : listen
# Enter second word : silent
# The words are anagrams