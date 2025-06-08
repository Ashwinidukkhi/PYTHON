# Write a function to check if a number is prime. 
# Return: True or False
# def is_prime(num):
#     if num<=1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#              return False
#     return True
# num=int(input("enter no:"))
# if is_prime(num):
#     print( f"{num} number is prime")
# else:
#     print(f"{num} number is not prime")

#QUE:Check if a number is prime using a loop. 
# # Input: A positive integer. 
# # Output: "Prime" or "Not Prime".

# n=int(input("A positive integer : "))      #  suppose n=7
# for i in range(2,n):                    #i=2,3,4,5,6
#     if n%i==0:                          #it check :7%2==0,7%3==0----7%6==0  //if remainder is =0 it is true than print no.is not prime
#         print("Not prime")
#         break                             # break is use for suppose  if condition is true print not prime otherwise  both are pint
# else:
#     print("Prime")

