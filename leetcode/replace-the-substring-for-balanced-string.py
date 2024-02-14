class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        start, count, required, current, index, result = 0, defaultdict(int), [0] * 4, [0] * 4, {'Q': 0, 'W': 1, 'E': 2, 'R': 3}, n

        for char in s:
            count[char] += 1

        for char, char_count in count.items():
            if char_count > n // 4:
                required[index[char]] = char_count - n // 4

        if required == [0, 0, 0, 0]:
            return 0

        for i, char in enumerate(s):
            current[index[char]] += 1

            if all(current[j] >= required[j] for j in range(4)):
                while True:
                    if s[start] in "QWER":
                        if current[index[s[start]]] > required[index[s[start]]]:
                            current[index[s[start]]] -= 1
                            start += 1
                        else:
                            break
                    else:
                        start += 1

                result = min(result, i - start + 1)

        return result
