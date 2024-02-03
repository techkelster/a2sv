class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appeared = {key: index for index, key in enumerate(s)}

        partitions = []
        start, end = 0, 0

        for i, key in enumerate(s):
            last_index = last_appeared[key]
            end = max(end, last_index)

            if i == end:
                partitions.append(i - start + 1)
                start = i + 1
        return partitions
        