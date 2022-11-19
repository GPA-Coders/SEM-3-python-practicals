import random

print("""
Scissors - 0
Rock - 1
Paper - 2
""")

choice = int(input("Enter your choice : "))
comp = random.randint(0, 2)

print("\nYour choice :", choice)
print("Computer's choice :", comp)

if choice == comp:
    print("Draw")
elif choice == 0 and comp == 1:
    print("You loose")
elif choice == 0 and comp == 2:
    print("You win")
elif choice == 1 and comp == 0:
    print("You win")
elif choice == 1 and comp == 2:
    print("You loose")
elif choice == 2 and comp == 0:
    print("You loose")
elif choice == 2 and comp == 1:
    print("YOu win")
else:
    print("Invalid choice!")

# Scissors - 0
# Rock - 1    
# Paper - 2   

# Enter your choice : 1

# Your choice : 1      
# Computer's choice : 1
# Draw