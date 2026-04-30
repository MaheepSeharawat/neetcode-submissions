class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=str()
        for i in s:
            if i.isalnum():
                t+=i
            else:
                continue
        i,j=0,len(t)-1
        t=t.lower()
        while (i<=j):
            if t[i]!=t[j]:
                return False
            i+=1
            j-=1
        return True
        
        

