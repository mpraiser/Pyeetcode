class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        candyCategory = set(candyType)
        half = len(candyType) // 2
        return len(candyCategory) if len(candyCategory) < half else half
