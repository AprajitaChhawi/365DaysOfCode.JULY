def cyclesort(arr,n):
    count=0
    for i in range(0,n-1):
        item=arr[i]
        pos=i
        for j in range(i+1,n):
            if arr[j]<item:
                pos=pos+1
        arr[pos],item=item,arr[pos]
        count=count+1
        while(pos!=i):
            pos=i
            for j in range(i+1,n):
                if arr[j]<item:
                    pos=pos+1
            arr[pos],item=item,arr[pos]
            count=count+1
    return arr,count
l=[8,7,9,5,4,1,2,3,6]
n=len(l)
l1,c=cyclesort(l,n)
print(l1)
print(c)
