class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count = Counter(s1)
        window_size = len(s1)

        for i in range(len(s2)):
            if s2[i] in char_count:
                char_count[s2[i]] -= 1

            if i >= window_size and s2[i - window_size] in char_count:
                char_count[s2[i - window_size]] += 1

            if all(count == 0 for count in char_count.values()):
                return True

        return False
        