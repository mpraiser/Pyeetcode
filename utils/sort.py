from typing import Iterator, List


def merge_sort(x: List) -> List:
    """
    Merge sort.
    Returns a new sorted list.
    """
    if len(x) <= 1:
        return x
    # if length >= 2, divide and conquer
    tmp = [0] * len(x)  # temporary place to save result
    mid = len(x) // 2
    part1 = merge_sort(x[:mid])
    part2 = merge_sort(x[mid:])
    i, j = 0, 0
    while i + j < len(x):
        if j >= len(part2) or (i < len(part1) and part1[i] <= part2[j]):
            tmp[i + j] = part1[i]
            i += 1
        else:
            # according to De Morgan's law, this condition equals to
            # j < len(part2) and (i >= len(part(1) or part1[i] > part2[j]))
            # equals to
            # (j < len(part2) and i >= len(part(1)) or (j < len(part2) and part1[i] > part2[j])
            tmp[i + j] = part2[j]
            j += 1
    return tmp


def quick_sort(x: List) -> List:
    pass


if __name__ == "__main__":
    case = [5,3,1,2,4]
    print(merge_sort(case))
