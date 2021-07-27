
# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        l=list(map(str,S.split('.')))
        low=0
        high=len(l)-1
        while(low<=high):
            l[low],l[high]=l[high],l[low]
            low=low+1
            high=high-1
        s=''
        for i in range(len(l)-1):
            s=s+l[i]
            s=s+'.'
        s=s+l[len(l)-1]
        return s
        # code here 

#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends
