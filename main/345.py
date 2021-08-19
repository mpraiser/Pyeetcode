from collections import deque


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ("a", "e", "i", "o", "u")
        stack = deque()
        for x in s:
            if x.lower() in vowels:
                stack.append(x)

        result = ""
        for x in s:
            if x.lower() in vowels:
                result += stack.pop()
            else:
                result += x

        return result
