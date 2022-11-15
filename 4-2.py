hours = int(input("Enter hours : "))
wage = float(input("Enter wage : "))

total = hours * wage

if hours > 40:
    total = 40 * wage
    total += (hours - 40)*(wage*1.5)
    
print("Your total pay is : ", total)

# Enter hours : 50
# Enter wage : 100
# Your total pay is :  5500.0