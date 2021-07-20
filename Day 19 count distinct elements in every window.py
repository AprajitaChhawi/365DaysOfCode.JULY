

class Solution:
    def length(self,m):
        count=0
        for idx,values in m.items():
            if m[idx]>=1:
                count=count+1
        return count
    def countDistinct(self, A, N, K):
        l=[]
        m={}
        ch=0
        count=0
        for i in range(k):
            if A[i] in m:
                m[A[i]]=m[A[i]]+1
            else:
                m[A[i]]=1
                count=count+1
        l.append(count)
        for i in range(k,n):
            if m[A[ch]]==1:
                count=count-1
            m[A[ch]]=m[A[ch]]-1
            ch=ch+1
            if A[i] not in m or m[A[i]]==0:
                count=count+1
                m[A[i]]=1
            elif A[i] in m:
                m[A[i]]=m[A[i]]+1
            l.append(count)
        return l
        # Code here

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends
