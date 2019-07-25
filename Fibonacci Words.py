"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler230/problem
""""
#python 3

#for smaller length of A and B and N

arr=[]

def fibo(a,b,n):
    
    a=str(a)
    b=str(b)
    c=a+b
    
    while len(c)<=n:
        
        c=a+b
        
        if len(c)>n:
            new_c=c[:n]
            print(new_c[-1])
            
            arr.append(c)
            
            
            break
        
            
        a=b
        b=c
        
    return 1
arr1=[]   
n=int(input())
for i in range(n):
    a,b,n=[int(x) for x in input().split()]
    arr1.append([a,b,n])
for i in range(len(arr1)):
    fibo(arr1[i][0],arr1[i][1],arr1[i][2])

#for any lenghth of A and B and N

def findlengthterm(n):

    if n==1:
        return len(A)
    elif n==2:
        return len(B)

    a=len(A)
    b=len(B)
    c=0
    i=2

    while i<n:
        c=a+b
        a=b
        b=c
        i+=1

    return c

def findIndex(n):

    if (n<=1):
        return n

    a=len(A)
    b=len(B)
    c=0
    res=2

    while c<n:
        c=a+b
        res+=1
        a=b
        b=c

    return res

num=int(input())
arr=[]

for i in range(num):

    A,B,x=input().split()
    s=int(x)
    n=findIndex(s)
    a=s

    while n>2:
        l=findlengthterm(n-2)

        if a>l:
            a=a-l
        else:
            n=n-1
        n=n-1

    if n==1:
        arr.append(A[a-1])
    else:
        arr.append(B[a-1])

for result in arr:
    print(result)
        
