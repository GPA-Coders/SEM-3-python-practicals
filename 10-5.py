hex_string = input("Enter hex value : ")

red = int(hex_string[0:2], 16)
green = int(hex_string[2:4], 16)
blue = int(hex_string[4:6], 16)

print(f"Red({red}) Green({green}) Blue({blue})")

# Enter hex value : FF6347
# Red(255) Green(99) Blue(71)