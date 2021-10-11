class Solution:
    def numberToWords(self, num: int) -> str:

        digit_en = {
            0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
            9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
            20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
        }
        weight_en = {
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

        def n2en(n: int) -> str:
            """convert int n (< 1000) to english"""
            hundreds, n = divmod(n, 100)
            ret = []
            if hundreds > 0:
                ret.append(f"{digit_en[hundreds]} {weight_en[100]}")
            if n <= 20:
                if not (n == 0 and hundreds > 0):
                    ret.append(f"{digit_en[n]}")
            else:
                tens, ones = divmod(n, 10)
                if tens > 0:
                    if ones > 0:
                        ret.append(f"{digit_en[tens * 10]} {digit_en[ones]}")
                    else:
                        ret.append(f"{digit_en[tens * 10]}")
            return " ".join(ret)

        items = []
        for weight in (1000000000, 1000000, 1000):
            value, num = divmod(num, weight)
            if value > 0:
                items.append(f"{n2en(value)} {weight_en[weight]}")
        if not (len(items) > 0 and num == 0):
            items.append(n2en(num))
        return " ".join(items)


cases = [
    123, 12345, 1234567, 1234567891, 100, 1000
]
for case in cases:
    ans = Solution().numberToWords(case)
    print(case, ans)
