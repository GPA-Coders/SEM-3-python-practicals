temp = {"Sunday" : 30, "Monday" : 35, "Tuesday" : 40, "Wednesday" : 45, "Thursady" : 50, "Friday" : 55, "Saturday" : 60}

print("The days on which temperature was between 40 and 50 dgrees :", end=" ")

for key in temp:
    if 40 <= temp[key] <= 50:
        print(key, end=" ")

# The days on which temperature was between 40 and 50 dgrees : Tuesday Wednesday Thursady