from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def f(left: int, right: int) -> int:
            """max length in [left, right)"""
            if left >= right:
                return 0
            solutions = set()
            visited = set()
            for i in range(left, right):
                if s[i] in visited:
                    continue
                visited.add(s[i])
                for j in reversed(range(i + 1, right + 1)):
                    # [i, j)
                    if s[i] == s[j - 1]:
                        if i < j - 1:
                            solutions.add(f(i + 1, j - 1) + 2)
                            # return f(i + 1, j - 1) + 2
                        else:
                            solutions.add(1)
                            # return 1
                        break
            return max(solutions)

        return f(0, len(s))


cases = [
    "bbbab",
    "cbbd",
    "a",
    "gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv "
]
for case in cases:
    ans = Solution().longestPalindromeSubseq(case)
    print(ans)

# ans = Solution().longestPalindromeSubseq(cases[3])
# print(ans)