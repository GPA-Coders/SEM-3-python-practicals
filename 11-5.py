f = open("11-5.txt", "r")
content = f.read()
f.close()

sentences = content.split(".")
content = content.replace(".", "")
words = content.split(" ")

sentence_sum = 0
word_sum = 0

for sentence in sentences:
    sentence_sum += len(sentence)

for word in words:
    word_sum += len(words)

print("Average word length :", word_sum//len((words)))
print("Average sentence length :", sentence_sum//len((sentences)))

# Average word length : 8
# Average sentence length : 11