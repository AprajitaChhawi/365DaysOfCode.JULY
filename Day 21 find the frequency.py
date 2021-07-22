#User function Template for python3

"""
You're given an array (arr) of length n
Return the frequency of element x in the given array
"""
def findFrequency (arr, n, x):
    count=0
    for i in arr:
        if i==x:
            count=count+1
    return count
    # Your Code Here


#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list (map (int, input ().split ()))
    x = int (input ())
    print (findFrequency (arr, n, x))
    

# } Driver Code Ends
