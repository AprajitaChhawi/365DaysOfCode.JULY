def sortString(s,n):
    count=[0]*26
    for i in range(n):
        count[ord(s[i])-ord('a')]=count[ord(s[i])-ord('a')]+1
    for i in range(26):
        if count[i]>0:
            print(chr(i+ord('a')),count[i])
sortString('abbcvgh',7)
