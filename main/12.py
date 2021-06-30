class Solution:
    def intToRoman(self, num: int) -> str:
        character = [
            ['I', 'V'],
            ['X', 'L'],
            ['C', 'D'],
            ['M']
        ]

        def get_bit(value, level):
            """
            Args:
                level: [0, +inf)
            """
            if level >= 3:
                return 'M' * value
            else:
                if value == 9:
                    return character[level][0] + character[level+1][0]
                elif value >= 5:
                    return character[level][1] + character[level][0] * (value - 5)
                elif value == 4:
                    return character[level][0] + character[level][1]
                else:
                    return character[level][0]*value

        ans = ''

        for i in reversed(range(4)):
            value = num // 10**i
            num %= 10**i
            ans += get_bit(value, i)
        
        return ans

x = Solution()
ans = x.intToRoman(58)
print(ans)

# ans = []
# for i in range(1, 3999+1):
#     ans.append(x.intToRoman(i))
# with open('table.txt', 'w') as fp:
#     fp.write(str(ans))
