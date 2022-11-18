dictionary = {"Gujarat" : "Gandhinagar", "Assam" : "Dispur", "Bihar" : "Patna", "Goa" : "Panaji", "Rajasthan" : "Jaipur"}

for key in dictionary:
    print("Enter the capital of", key, ":", end=" ")
    ans = input()

    if dictionary[key] == ans:
        print("Correct!\n")
    else:
        print("Incorrect!\n")

# Enter the capital of Gujarat : Ahmedabad
# Incorrect!

# Enter the capital of Assam : Dispur
# Correct!

# Enter the capital of Bihar : Odissa
# Incorrect!

# Enter the capital of Goa : Panaji
# Correct!

# Enter the capital of Rajasthan : Kachch
# Incorrect!