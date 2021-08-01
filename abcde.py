def solve(A, B):
    l=[]
    for k in B:
        if k[0]==2:
            l1=k[1]-1
            l2=k[2]-1
            for i in range(l1,l2+1):
                for j in range(i,l2+1):
                    a=[]
                    max_s=0
                    s=0
                    for k in range(i,j+1):
                        a.append(A[k])
                        s1=0
                        s2=0
                        for i in range(len(a)):
                            if i%2==0:
                                s1=s1+a[i]
                            else:
                                s1=s1-a[i]
                        for i in range(len(a)):
                            if i%2!=0:
                                s2=s2+a[i]
                            else:
                                s2=s2-a[i]
                    s=max(s,s1,s2)
                    max_s=max(s,max_s)
            l.append(max_s)
        else:
            if k[1]==0:
                A[k[1]]=k[2]
            else:
                A[k[1]-1]=k[2]
    return l
A=[2,4,-10,3,7]
B=[[2,1,2],[2,3,4],[2,1,5],[2,2,3]]
l=solve(A,B)
print(l)
