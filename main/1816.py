class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # return " ".join(s.split()[:k])
        count = 0
        end = len(s) # default return all s
        for i, x in enumerate(s):
            if x == " ":
                count += 1
                if count == k:
                    end = i
                    break
        return s[:end]


cases = [
    ("Hello how are you Contestant", 4),
    ("chopper is not a tanuki", 5)
]
for case in cases:
    ans = Solution().truncateSentence(*case)
    print(ans)
