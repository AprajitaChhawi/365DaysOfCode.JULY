
#User function Template for python3


class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, n): 
        for i in range(n):
            for j in range(i+1,n):
                a[i][j],a[j][i]=a[j][i],a[i][j]
        for i in range((n//2)):
            a[i],a[n-i-1]=a[n-i-1],a[i]
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends
