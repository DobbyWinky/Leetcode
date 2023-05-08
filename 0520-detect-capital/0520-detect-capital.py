class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1 or len(word)==0:
            return True
        firstCapital=True if word[0].isupper() else False
        secondCapital=True if word[1].isupper() else False
        if not firstCapital and secondCapital:
            return False
        for i in range(2, len(word)):
            if secondCapital and word[i].islower():
                return False
            if not secondCapital and word[i].isupper():
                return False
        return True
            
        