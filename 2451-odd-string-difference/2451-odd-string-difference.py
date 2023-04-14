class Solution:
    def oddString(self, words: List[str]) -> str:
        hash=collections.defaultdict(list)
        for i in range(len(words)):
            h=[]
            for j in range(len(words[i])-1):
                h.append(ord(words[i][j])-ord(words[i][j+1]))
            hash[tuple(h)].append(words[i])
        for k in hash:
            if len(hash[k])==1:
                return hash[k][0]
        return ""
        