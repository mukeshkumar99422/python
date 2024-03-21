#s=1+5+15+...n times
def sum1(n):
    s=1
    for i in range(1,n):
        s=s+(i*5)
    return s
    
#s=1+5+15+...upto n
def sum2(n):
    s=1
    i=5
    while i<=n:
        s=s+i
        i=i+5
    return s

#s=2+4+6+...n times
def sum3(n):
    s=0
    for i in range(1,n+1):
        s=s+(2*i)
    return s
    
#s=1-3+5-...upto n
def sum4(n):
    s=0
    i=1
    while i<=n:
        if(s%2==0):
            s=s+i
        else:
            s=s-i
        i=i+2
    return s

n=int(input("Enter value of n:"))
print("1st sum:",sum1(n))
print("2nd sum:",sum2(n))
print("3rd sum:",sum3(n))
print("4th sum:",sum4(n))
