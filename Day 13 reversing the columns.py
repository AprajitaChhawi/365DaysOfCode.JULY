#User function Template for python3

class Solution:
    
    #Function to reverse the columns of a matrix.
    def reverseCol(self,matrix):
        n=len(matrix)
        for i in range(n):
            a=matrix[i]
            a=a[::-1]
            matrix[i]=a
        return matrix
        # code here 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n1,m1 = map(int,input().strip().split())
        matrix = [[0 for j in range(m1)] for i in range(n1)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(n1):
            for j in range (m1):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.reverseCol(matrix)
        for i in range(n1):
            for j in range(m1):
                print(matrix[i][j],end=" ")
        print()
        

# } Driver Code Ends
