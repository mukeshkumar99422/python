def pat(n):
    m=n-1
    for i in range(1,n+1):
        for j in range(1,(n-i)+1):
            print(" ",end="")
        
        a=1
        for j in range(1,i+1):
            print(a,end="")
            if(a==9):
                a=0
            else:
                a=a+1
        
        if(a<2):
            b=a+8
        else:
            b=a-2
        for j in range(1,i):
            print(b,end="")
            if(b==9):
                b=0
            else:
                b=b+1
        
        print("\n")

n=int(input("Enter no: of lines in pattern:"))   
pat(n)
