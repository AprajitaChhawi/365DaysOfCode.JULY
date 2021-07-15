#User function Template for python3

class Solution:
    def merged(self,a,b,n,m):
        i=0
        j=0
        l=[]
        while(i<n and j<m):
            if a[i]<b[j]:
                l.append(a[i])
                i=i+1
            elif a[i]>b[j]:
                l.append(b[j])
                j=j+1
            else:
                l.append(a[i])
                l.append(a[i])
                i=i+1
                j=j+1
        while(i<n):
            l.append(a[i])
            i=i+1
        while(j<m):
            l.append(b[j])
            j=j+1
        return l
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        if(len(arr))==1:
            return arr[0]
        elif (len(arr)==2):
            return self.merged(arr[0],arr[1],len(arr[0]),len(arr[1]))
        else:
            while(len(arr)!=1):
                a=arr.pop()
                b=arr.pop()
                p=len(a)
                m=len(b)
                c=self.merged(a,b,p,m)
                arr.append(c)
        return arr[0]
        # code here
        # return merged list

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        numbers=[[ 0 for _ in range(n) ] for _ in range(n) ]
        line=input().strip().split()
        for i in range(n):
            for j in range(n):
                numbers[i][j]=int(line[i*n+j])
        ob = Solution();
        merged_list=ob.mergeKArrays(numbers, n)
        for i in merged_list:
            print(i,end=' ')
        print()
# } Driver Code Ends
