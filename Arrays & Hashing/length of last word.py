class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trim = s.rstrip()
        words = trim.split(' ')
        last_word = words[-1] if words else ""
        return len(last_word)
        
