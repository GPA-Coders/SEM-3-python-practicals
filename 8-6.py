def emi(p, r, t):
	r = r / (12 * 100)
	t = t * 12
	emi = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
	return emi

principal = int(input("Enter principal : "))
rate = int(input("Enter rate of interest : "))
time = int(input("Enter time in years : "))
emi = emi(principal, rate, time)
print("Monthly EMI is :", emi)

# Enter principal : 10000
# Enter rate of interest : 10
# Enter time in years : 2
# Monthly EMI is : 461.44926337516654