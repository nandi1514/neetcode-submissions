class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def countLetters(string):
            count = dict()
            for i in range(len(string)):
                if string[i] in count:
                    count[string[i]] += 1
                else:
                    count[string[i]] = 1
            return count

        return countLetters(s) == countLetters(t)
