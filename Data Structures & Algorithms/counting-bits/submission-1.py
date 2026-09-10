class Solution:
    def countBits(self, n: int) -> List[int]:
        keys = [i for i in range(n+1)] 
        range_dict = dict(zip(keys, range(len(keys))))
        counts_list = []
        for key, value in range_dict.items():
            range_dict[value] = f"{key:b}"
        for value in range_dict.values():
            counts_list.append(value.count('1'))

        return counts_list