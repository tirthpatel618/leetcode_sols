#medium pretty good one

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count_letters(word):
            letters = [0] * 26
            for letter in word:
                letters[ord(letter) - ord('a')] += 1
            return letters
        
        max_letters = [0] * 26
        for word in words2:
            for i, l in enumerate(count_letters(word)):
                max_letters[i] = max(max_letters[i], l)
        
        res = []
        for word in words1:
            if all(x >= y for x, y in zip(count_letters(word), max_letters)):
                res.append(word)
        return res



class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = set(words1)
        letters = {}
        for i in words2:
            for j in i:
                count = i.count(j)
                if j not in letters or count > letters[j]:
                    letters[j] = count
        for i in words1:
            for j in letters:
                if i.count(j) < letters[j]:
                    ans.remove(i)
                    break
        return list(ans)