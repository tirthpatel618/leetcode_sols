class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = list(s)
        length = len(letters)
        changes = [0 for _ in range(length)]
        for shift in shifts:
            if shift[2] == 1:
                changes[shift[0]] += 1
                if shift[1] + 1 < length:
                    changes[shift[1] + 1] -= 1
            else:
                changes[shift[0]] -= 1
                if shift[1] + 1 < length:
                    changes[shift[1] + 1] += 1
        num_shifts = 0
        for i in range(length):
            num_shifts = (num_shifts + changes[i]) % 26
            if num_shifts < 0:
                num_shifts += 26

            shifted_char = chr(
                (ord(s[i]) - ord("a") + num_shifts) % 26 + ord("a"))
            letters[i] = shifted_char
        return "".join(letters)