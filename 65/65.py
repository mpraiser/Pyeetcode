from enum import Enum


class State(Enum):
    start = 'start'
    s1 = 's1'
    d = 'd'
    dn1 = 'dn1'
    n1 = 'n1'
    n1d = 'n1d'
    e = 'e'
    s2 = 's2'
    n2 = 'n2'
    error = 'error'


class Solution:
    transfer = {
        State.start: {
            'sign': State.s1,
            'number': State.n1,
            'E': State.error,
            '.': State.d
        },
        State.s1: {
            'sign': State.error,
            'number': State.n1,
            'E': State.error,
            '.': State.d
        },
        State.d: {
            'sign': State.error,
            'number': State.dn1,
            'E': State.error,
            '.': State.error
        },
        State.n1: {
            'sign': State.error,
            'number': State.n1,
            'E': State.e,
            '.': State.n1d
        },
        State.n1d: {
            'sign': State.error,
            'number': State.n1d,
            'E': State.e,
            '.': State.error
        },
        State.dn1: {
            'sign': State.error,
            'number': State.dn1,
            'E': State.e,
            '.': State.error
        },
        State.e: {
            'sign': State.s2,
            'number': State.n2,
            'E': State.error,
            '.': State.error
        },
        State.s2: {
            'sign': State.error,
            'number': State.n2,
            'E': State.error,
            '.': State.error
        },
        State.n2: {
            'sign': State.error,
            'number': State.n2,
            'E': State.error,
            '.': State.error
        },
    }

    def __init__(self):
        self.state = State.start

    def isNumber(self, s: str) -> bool:
        for x in s:
            self.check(x)
            if self.state == State.error:
                return False
        return self.state in (State.n1, State.dn1, State.n2, State.n1d)

    @staticmethod
    def preprocess(x: str) -> str:
        if x in ('+', '-'):
            return 'sign'
        if x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return 'number'
        if x in ('e', 'E'):
            return 'E'
        else:
            return x

    def check(self, x: str):
        key = self.preprocess(x)
        if key in self.transfer[self.state]:
            self.state = self.transfer[self.state][key]
        else:
            self.state = State.error


cases = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1",
         "53.5e93", "-123.456e789", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

for case in cases:
    ans = Solution().isNumber(case)
    print(case, ans)