# Write a function that returns the LCM (Least Common Multiple) of two numbers using a 
# loop.
# def lcm1(a,b):
#     n=max(a,b)
#     lcm=n
#     while True:
#         if lcm%a==0 and lcm%b==0:
#             return lcm
#         lcm+=n
# n1=int(input("enter no.:") )
# n2=int(input("enter no.:") )
# result=lcm1(n1,n2)
# print("LCM:",result)

# -----------------------------------------------------------------------------
# Find the Least Common Multiple (LCM) 
# Write a function to calculate the least common multiple (LCM) of two numbers.  
# Use the formula:   
# `LCM(a, b) = (|a * b|) / GCD(a, b)` 
# Input Format 
# Input: Two integers a and b. 
# Output Format 
# Output: The least common multiple of a and b.
def f_gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def f_lcm(a,b):
    gcd=f_gcd(a,b)
    lcm=(a*b)//gcd
    return lcm
a=int(input("enter no") )
b=int(input("enter no"))
lcm=f_lcm(a,b)
print("lcmof",a,"lcm of" ,b,"is",lcm)

