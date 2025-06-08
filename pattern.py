#---------------pattern Qno.1--------------------------------
# *
# **
# ***
# ****
# *****
# for i in range (0,5): 
#     for j in range(i):
#           print("*",end=" ")  
#     print("*")       

# -------------------pattern Qno.2---------------------------
# *****
#  ****
#   ***
#    **
#     *
# for i in range(5):
#     print(" "*i +"*"*(5-i))


# ---------------------pattern Qno.1 :by user input-----------
# n=int(input("enter no.:"))
# for i in range(n):
#     for j in range(i):
#         print("*",end=" .")
#     print("*")


# ---------------------pattern Qno.3--------------------------
# 1
# 12
# 123
# 1234
# 12345
# n=int(input("enter no."))
# for i in range(1,n+1):  #if enter 5 than the programme run 1 to 5 || each no. of i represent a row(outer loop)
#     for j in range(1,i+1):#print no. 1 up to i on each row(inner loop)
#         print(j,end='')  #print no. same line &move to next new line
#     print()          # move curser to the nextLine


# ------------------pattern Qno.4-----------------------------
# A
# ABC
# ABCD
# ABCDE
# n=5 enter i/o
# n=int(input("enter no.:"))
# for i in range(1,n+1): #if enter 5 loop run 1 to 5
#     for j in range(65,65+i):  #why give 65? : b/c 65 is a ascci value of A
#                             #  when   i=1 j goes from 65 to 65 print A the process will going
#         print(chr(j),end=' ') # end=" " means not move next line  after printing
#     print()

# ---------------------print 1 to 100 no.that divisible by 7bt not 5----------------------
# n1=int(input("start :"))#enter 1
# n2=int(input("end:"))#enter 100
# for i in range(n1,n2+1): #  the line print 1 to 101
#     if i%7==0 and i%5!=0: #if 1 
#       print(i)

# --------------------------------reverse no. using arthmatic opr-------------------------
# i/p =2314
# o/p =4132
# n=input("enter no.:")
# a=n[::-1]#it is slicing,start from end ,go back trough string& -1 is step
# print(a)

# ---------------------------.Qesno.print prime no--------------------------------------------
# k=int(input("start :")) 
# print("prime no.2 to 10:",k)  #enter no 10,print no. 1 to 10
# for num in range(2,k+1):   #if enter no.10 loop chek 2 to 10
#     is_prime=True   #assume num is prime
#     for i in range(2,int(num**0.5)+1):#if num is divisible by any num to 2 to square root of number 
#         if num%i==0:
#             is_prime=False#if it is divisible its not prime ,so set is_prime=false
#             break
#     if is_prime:  #if no divisor found  (is _prime is still true ) ,print number    
#       print(num)  

# Continuous Numbers in Triangle: 
# Input:10 
# Output: 
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10
# n=int(input())
# x=1
# row=1
# while x<=n:
#     for i in range(row):
#         if x>n:
#             break
#         print(x,end=' ')
#         x+=1
#     print()
#     row+=1

