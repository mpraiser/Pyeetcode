class Solution:
    @staticmethod
    def left_right_align(words: list[str], words_len: int, maxWidth: int) -> str:
        sentence = words[0]
        blank = maxWidth - words_len
        if len(words) == 1:
            sentence += " " * blank
            return sentence
        sep = blank // (len(words) - 1)
        seps = [sep] * (len(words) - 1)
        seps_len = sep * (len(words) - 1)
        blank -= seps_len
        i = 0
        while blank > 0:
            seps[i] += 1
            blank -= 1
            i = (i + 1) % len(seps)
        for i in range(1, len(words)):
            sentence += " " * seps[i - 1]
            sentence += words[i]
        return sentence

    @staticmethod
    def left_align(words: list[str], words_len: int, maxWidth: int):
        sentence = " ".join(words)
        sentence += " " * (maxWidth - len(sentence))
        return sentence

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:

        sentences = []
        word_prep = []
        word_prep_len = 0
        i = 0
        while i < len(words):
            word = words[i]
            if len(word) + len(word_prep) + word_prep_len <= maxWidth:
                word_prep.append(word)
                word_prep_len += len(word)
                i += 1
            else:
                # form a sentence
                sentences.append(self.left_right_align(word_prep, word_prep_len, maxWidth))
                word_prep = []
                word_prep_len = 0
        if len(word_prep) > 0:
            sentences.append(self.left_align(word_prep, word_prep_len, maxWidth))
        return sentences


cases = [
    (["This", "is", "an", "example", "of", "text", "justification."], 16),
    (["What", "must", "be", "acknowledgment", "shall", "be"], 16),
    (["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do", "for",
      "your", "country"], 16)
]

for case in cases:
    ans = Solution().fullJustify(*case)
    print(ans)

# ans = Solution().fullJustify(*cases[2])
# print(ans)
