def fibo(n):#def name(parameter)
    x=0
    y=1
    for i in range(1,n): 
        z=x+y
        x=y
        y=z
        print(z)
fibo(34)#pass argument