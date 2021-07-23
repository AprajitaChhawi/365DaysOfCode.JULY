def algo(s,c,n):
    m={}
    cost=0
    m[s[0]]=c[0]
    for i in range(1,n):
        if s[i-1]==s[i] and s[i-1] in m:
            cost=cost+min(m[s[i-1]],c[i])
            m[s[i]]=c[i]
        else:
            m[s[i]]=c[i]
    return cost
t=int(input())
while t:
    t=t-1
    n=int(input())
    s=input()
    c=list(map(int,input().split()))
    c1=algo(s,c,n)
    print(c1)
