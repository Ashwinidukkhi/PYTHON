#  q.4Check if a number is a palindrome using a loop. 
# Input: 121 → Output: Palindrome 
# Input: 123 → Output: Not Palindrome
# define a function is palindrome
def ispalindrome(n): 
    a=str(n)
    reversenum=a[::-1]
    return a==reversenum
# user input
n=int(input("enter:"))
# check n is palindrome and print
if ispalindrome(n):
    print(f"{n} is  palindrome")
else:
    print(f"{n} is not  palindrome") 