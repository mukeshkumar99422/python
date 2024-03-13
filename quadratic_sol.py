import math

def sol(a,b,c):
    r=[0,0]
    D=((pow(b,2))-(4*a*c))
    if D==0:
        r[0]=r[1]=(-b)/(2*a)
    elif D>0:
        r[0]=((-b)+math.sqrt(D))/(2*a)
        r[1]=((-b)-math.sqrt(D))/(2*a)
    else:
        r[0]=complex((-b)/(2*a),(math.sqrt(-D)/(2*a)))
        r[1]=complex((-b)/(2*a),-(math.sqrt(-D)/(2*a)))
        
    return r
    
print("ax^2+bx+c")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
r=sol(a,b,c)

print("Roots of the equation are:",r[0],", ",r[1])
