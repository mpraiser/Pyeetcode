"""
提供Leetcode风格的对象序列化/字符串解析方法
"""
from typing import List


def serialize(values: List) -> str:
    for i in range(len(values)):
        if values[i] is None:
            values[i] = "null"
        else:
            values[i] = str(values[i])
    return "[" + ",".join(values) + "]"


def parse(s: str) -> List:
    """parse string s to List[int or None]"""
    if not (s[0] == "[" and s[-1] == "]"):
        raise ValueError("Not a valid Expression.")

    if len(s) < 3:
        return []

    values: str = s[1:-1].replace(" ", "")
    values: List = values.split(",")

    for i in range(len(values)):
        if values[i] == "null":
            values[i] = None
        else:
            values[i] = int(values[i])

    return values


if __name__ == "__main__":
    result = parse("[5, 4, 7, 3, null, 2, null, -1, null, 9]")
    print(serialize(result))
