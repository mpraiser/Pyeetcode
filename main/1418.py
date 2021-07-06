from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        counter = dict()
        dishes = set()
        for order in orders:
            (_, table, dish) = order
            if dish not in dishes:
                dishes.add(dish)
            if table not in counter:
                counter[table] = dict()
            if dish not in counter[table]:
                counter[table][dish] = 1
            else:
                counter[table][dish] += 1
                
        dishes = sorted(dishes)
        tables = sorted(counter.keys(), key=lambda x: int(x))
        result = [["Table", *dishes]]
        for table in tables:
            row = [table]
            for dish in dishes:
                if dish in counter[table]:
                    row.append(str(counter[table][dish]))
                else:
                    row.append('0')
            result.append(row)
        return result


ans = Solution().displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])
print(ans)