from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        elif len(matrix[0]) == 0:
            return []

        
        i_min = 0
        i_max = len(matrix)
        j_min = 0
        j_max = len(matrix[0])

        def in_border(i, j):
            return i_min <= i < i_max and j_min <= j < j_max

        def next_i_j(i, j, direction):
            if direction == 0:
                return i, j+1
            elif direction == 1:
                return i+1, j
            elif direction == 2:
                return i, j-1
            elif direction == 3:
                return i-1, j

        def next_direction(direction):
            return (direction + 1) % 4

        direction = 0  # 0: right, 1: down, 2: left, 3: up
        i, j = 0, 0
        result = []
        
        while True:
            result.append(matrix[i][j])

            counter = 0  # number to change direction since last draw
            while counter < 4:
                next_i, next_j = next_i_j(i, j, direction)
                if in_border(next_i, next_j):
                    i, j = next_i, next_j
                    break
                else:
                    if direction == 0:
                        i_min += 1
                    elif direction == 1:
                        j_max -= 1
                    elif direction == 2:
                        i_max -= 1
                    elif direction == 3:
                        j_min += 1
                    direction = next_direction(direction)
                    counter += 1
            if counter >= 4:
                break    
                
        return result



ans = Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(ans)