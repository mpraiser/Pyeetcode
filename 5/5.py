from math import ceil

class Solution:
    def longestPalindrome(self, s: str) -> str:
        results = []

        def check_even(p, stack):
            # left = p - 1
            # right = p

            i = 1
            while len(stack)-1-i >= 0 and p+i < len(s) and stack[-1-i] == s[p+i]:
                i += 1
            i -= 1
            results.append(s[p-1-i:p+i+1])

        def check_odd(p, stack):
            # left = p - 1
            # right = left

            i = 1
            while len(stack)-2-i >= 0 and p+i < len(s) and stack[-2-i] == s[p+i]:
                i += 1
            
            i -= 1
            results.append(s[p-2-i:p+i+1])

        def search(p: int):
            """
            p: present index
            """

            stack = ''
            for i in range(len(s)):
                # a b c | c ...                    
                if len(stack) >= 1 and s[i] == stack[-1]:
                    # find start point of palindrome
                    check_even(i, stack)
                # a b c | b ...
                if len(stack) >= 2 and s[i] == stack[-2]:
                    check_odd(i, stack)
                stack += s[i]

        # get all results
        search(0)
        # find result with max length
        if results:
            max_len = len(results[0])
            max_ptr = 0
            for i in range(len(results)):
                if len(results[i]) > max_len:
                    max_len = len(results[i])
                    max_ptr = i
            return results[max_ptr]
        else:
            return s[0]
                    
x = Solution()
result = x.longestPalindrome("caba")
print(result)