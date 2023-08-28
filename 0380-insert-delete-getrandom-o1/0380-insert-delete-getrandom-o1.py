class RandomizedSet:

    def __init__(self):
        self.arr=[]
        self.hash=collections.defaultdict(int)
        

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.arr.append(val)
        self.hash[val]=len(self.arr)-1
        return True

        

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        idx=self.hash[val]
        
        self.arr[idx]=self.arr[-1]
        self.hash[self.arr[idx]]=idx
        self.arr.pop()
        del self.hash[val]
        return True

    def getRandom(self) -> int:
        randVal=random.randint(0, len(self.arr)-1)
        return self.arr[randVal]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()