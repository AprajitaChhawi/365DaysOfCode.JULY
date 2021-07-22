#code
def sorting(l,n):
    m={}
    l1=[]
    for i in l:
        if i in m:
            m[i]=m[i]+1
        else:
            m[i]=1
    a=sorted(m.items(), key=lambda x: x[1],reverse=True)
    for idx,value in a:
        while(value):
            l1.append(idx)
            value=value-1
    return l1
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    k=sorting(l,n)
    for i in k:
        print(i,end=" ")
    print()
