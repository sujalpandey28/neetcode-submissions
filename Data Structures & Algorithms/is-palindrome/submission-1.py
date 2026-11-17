class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            while (i<j and not self.alphanum(s[i])):
                i+=1
            while (i<j and not self.alphanum(s[j])):
                j-=1
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
            

        

    def alphanum(self,n):
        return (ord("A")<=ord(n)<=ord("Z") or
                ord("a")<=ord(n)<=ord("z") or
                ord("0")<=ord(n)<=ord("9"))
