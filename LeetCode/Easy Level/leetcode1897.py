class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        all_chars = "".join(words)
        char_set = set(all_chars)

        for i in char_set:
            if all_chars.count(i) % len(words) != 0:
                return False
        return True
    
