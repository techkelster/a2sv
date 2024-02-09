class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        contaner = Counter()
        left = max_length = 0

        for right in range(len(s)):
            contaner[s[right]] += 1
            max_length = max(max_length, contaner[s[right]])

            if right - left + 1 > k + max_length:
                contaner[s[left]] -= 1
                left += 1

        return right - left + 1