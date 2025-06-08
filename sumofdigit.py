#Find the sum of digits of a number using a loop. 
# Input: 1234 
# Output: 10
num = int(input())
sum = 0  #we declare sum=0
# Loop to extract digits and add to sum
while num > 0:          #1234>0 
    n= num % 10         # Get the last digit
    sum+= n             # we get sum of digit 
    num = num // 10     
print("Sum of digits:",sum )
