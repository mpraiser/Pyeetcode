class Solution:
    value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        i = 0
        ans = 0
        while i < len(s):
            if i < len(s)-1 and Solution.value[s[i]] < Solution.value[s[i+1]]:
                ans -= Solution.value[s[i]]
            else:
                ans += Solution.value[s[i]]
            i += 1
    
        return ans

x = Solution()
r = x.romanToInt('IV')
print(r)

