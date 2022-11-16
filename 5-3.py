for i in range(5):
    for k in range(4 - i):
        print(" ", end="")
    for j in range(0, i+1):
        print("*", end=" ")
    print()

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#     * 
#    * *
#   * * *
#  * * * *
# * * * * *
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5