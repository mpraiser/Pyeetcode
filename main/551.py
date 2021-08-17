class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        absent = 0
        for x in s:
            if x == "L":
                late += 1
                if late >= 3:
                    return False
            else:
                late = 0
                if x == "A":
                    absent += 1
                    if absent >= 2:
                        return False
        return True


cases = [
    "PPALLP",
    "PPALLL"
]

for case in cases:
    ans = Solution().checkRecord(case)
    print(ans)