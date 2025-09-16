class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        words = text.split(" ")
        count = 0

        for word in words:
            if not any(ch in broken for ch in word):
                count += 1
        return count

        broken = [False] * 26
        for b in brokenLetters:
            broken[ord(b) -97] = True
        
        count = 0
        wordBroken = True
        for c in text:
            if c == ' ':
                if not wordBroken:
                    count += 1
                wordBroken = False
            else:
                if not wordbroken and broken[ord(c) - 97]:
                    wordbroken = True
        if not wordBroken:
            count += 1
        return count