#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        n=len(A)
        m=len(B)
        i=0
        j=0
        while(i<n and j<m):
            if A[i]==B[j]:
                i=i+1
            j=j+1
        return i==n
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A,B = input().split()
        ob = Solution()
        if ob.isSubSequence(A,B):
            print(1)
        else:
            print(0)

# } Driver Code Ends
