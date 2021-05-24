class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in address:
            if (i == "."):
                i = "[.]"
            ans += i
        return ans
        
            