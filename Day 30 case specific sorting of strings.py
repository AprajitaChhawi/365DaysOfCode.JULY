
#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        case=[]
        lower=[]
        upper=[]
        for i in s:
            if i.isupper():
                case.append('U')
                upper.append(i)
            else:
                case.append('L')
                lower.append(i)
        upper.sort()
        lower.sort()
        idx=0
        s=''
        for i in case:
            if i=='U':
                s=s+upper.pop(0)
            else:
                s=s+lower.pop(0)
            idx=idx+1
        return s
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends
