#  Print a square matrix of numbers with diagonals as 0: 
# 1  2  3  4 
# 5  0  0  8 
# 9  0  0 12 
# 13 14 15 16 
# Hint : 1  Use nested for loops: one for rows (i) and one for columns (j). 
# 2 .Maintain a counter variable (e.g., num) to print increasing numbers from 1. 
# 3. Set the value to 0 only when the current element is on the main diagonal (i == j) or anti
# diagonal (i + j == n - 1). 
# 4. Otherwise, print the current number and increment it..

n=int(input("enter size:"))
x=1 #count variable that are icreament by 1
for i in range(n):
    for j in range(n):
        # for x in range(1):
            if i==j or i+j==n-1:
                 print(0,end=" ")
            else:
                 print(1,end=" ")
                 x+=1
    print()
