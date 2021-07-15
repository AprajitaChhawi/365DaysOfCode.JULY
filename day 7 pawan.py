def fun(s, a, b, u):
    if b > 0:
        return (a+b)*u
    else:
        count1 = s.count('10')
        count2 = s.count('01')
        c = min(count1, count2)
        return a*u + b*(c+1)

t = int(input())
while t:
    t=t-1
    u,a,b=map(int,input().split())
    s = input()
    op = fun(s, a, b, u)
    print(op)
