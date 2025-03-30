# This is a program to calculate simple interest 

def simple_intrest(p, n, r):
    """"This function calculates SI and A"""
    i = (p*n*r)/ 100
    a = p + i
    return i, a

# Take p, n, r as input from user
p = float(input("Please enter Principal in INR :"))
n = int(input("Please enter number of years :"))
r = float(input("Please enter rate of Interest in % p.a. :"))

# Call SImple interest function
i, a =simple_intrest(p, n, r)

# Show results
print(f"Simple Inetrest: {i:.2f} INR")
print(f"Ampunt : {a :.2f} INR")
