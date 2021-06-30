class Solution:
    states = ['start', 'space1', 'signed1', 'n1', 'n1d', 'd', 'e', 'dn1', 'signed2', 'n2', 'space2', 'error']
    transfer = {
            "start": {
                " ": "space1",
                ".": "d",
                "sign": "signed1",
                "number": "n1",
                "e": "error"
            },
            "signed1": {
                " ": "error",
                ".": "d",
                "sign": "error",
                "number": "n1",
                "e": "error"
            },
            "space1": {
                " ": "space1",
                ".": "d",
                "sign": "signed1",
                "number": "n1",
                "e": "error"
            },
            "d": {
                " ": "error",
                ".": "error",
                "sign": "error",
                "number": "dn1",
                "e": "error"
            },
            "dn1": {
                " ": "space2",
                ".": "error",
                "sign": "error",
                "number": "dn1",
                "e": "e"
            },
            "n1": {
                " ": "space2",
                ".": "n1d",
                "sign": "error",
                "number": "n1",
                "e": "e"
            },
            "n1d": {
                " ": "space2",
                ".": "error",
                "sign": "error",
                "number": "n1d",
                "e": "e"
            },
            "e": {
                " ": "error",
                ".": "error",
                "sign": "signed2",
                "number": "n2",
                "e": "error"
            },
            "signed2": {
                " ": "error",
                ".": "error",
                "sign": "error",
                "number": "n2",
                "e": "error"
            },
            "n2": {
                " ": "space2",
                ".": "error",
                "sign": "error",
                "number": "n2",
                "e": "error"
            },
            "space2": {
                " ": "space2",
                ".": "error",
                "sign": "error",
                "number": "error",
                "e": "error"
            }
        }

    def __init__(self):
        self.state = 'start'
        
        
    def isNumber(self, s: str) -> bool:
        for x in s:
            self.check(x)
            if self.state == 'error':
                return False
        if self.state in ('e', 'signed1', 'signed2', 'd', 'space1', 'start'):
            return False
        return True
            
    def check(self, x: str):
        key = self.preprocess(x)
        if key in self.transfer[self.state]:
            self.state = self.transfer[self.state][key]
        else:
            self.state = 'error'
    
    def preprocess(self, x: str) -> bool:
        if x == " " or x == '.': 
            return x
        elif x == 'e' or x == 'E':
            return 'e'
        elif x in ('+', '-'):
            return "sign"
        elif x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return "number"
        else:
            return None


cases = ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123", "12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]

for case in cases:
    ans = Solution().isNumber(case)
    print(ans)
        
