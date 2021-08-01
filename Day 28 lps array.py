def lps(s):
    l=[]
    n=len(s)
    l.append(0)
    i=1
    le=0
    while(i<n):
        if s[i]==s[le]:
            l.append(le+1)
            le=le+1
            i=i+1
        else:
            if le==0:
                l.append(0)
                i=i+1
            else:
                le=l[le-1]
    return l
print(lps('bba'))

