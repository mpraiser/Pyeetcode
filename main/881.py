class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        boat = 0
        count = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            boat += people[j]
            j -= 1
            if boat + people[i] <= limit:
                boat += people[i]
                i += 1
            boat = 0
            count += 1
        if boat > 0:
            count += 1
        return count


cases = [
    ([1, 2], 3),
    ([3, 2, 2, 1], 3),
    ([3, 5, 3, 4], 5),
    ([2, 49, 10, 7, 11, 41, 47, 2, 22, 6, 13, 12, 33, 18, 10, 26, 2, 6, 50, 10], 50)
]

# for case in cases:
#     ans = Solution().numRescueBoats(*case)
#     print(ans)

ans = Solution().numRescueBoats(*cases[3])
print(ans)
