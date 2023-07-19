class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        i=0
        while i<min(len(v1),len(v2)):
            if int(v1[i])<int(v2[i]):
                return -1
            elif int(v1[i])>int(v2[i]):
                return 1
            i+=1
        while i<len(v2) and int(v2[i])==0:
            i+=1
        while i<len(v1) and int(v1[i])==0:
            i+=1
        if i<len(v1):
            return 1
        if i<len(v2):
            return -1
        return 0
            
        