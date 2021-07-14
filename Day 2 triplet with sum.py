def findtriplets(arr, n):
    m={}
    for i in arr:
        if i in m:
            m[i]=m[i]+1
        else:
            m[i]=1
    for i in range(0,n):
        a=arr[i]
        for j in range(i,n):
            s=a+arr[j]
            k=0-s
            if arr[j]==k:
                if m[arr[j]]>1 and k in m:
                    return 1
            elif arr[i]==k:
                if m[arr[i]]>1 and k in m:
                    return 1
            elif arr[i]==arr[j]:
                if m[arr[i]]>1 and k in m:
                    return 1
            else:
                if k in m:
                    print(arr[i],arr[j],k)
                    return 1
    return 0
t=int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    print(findtriplets(l,n))
