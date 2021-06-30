class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        for n in nums:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        return odds + evens