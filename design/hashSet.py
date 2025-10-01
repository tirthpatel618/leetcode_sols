class MyHashSet:

    def __init__(self):
        self.hashSet = []

    def binary_search(self, hashSet, key):
        left = 0
        right = len(hashSet) - 1
        while left <= right:
            mid = (left + right) // 2
            if hashSet[mid] == key:
                #contains = true. and the index
                return (True, mid)
            elif hashSet[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        #contains is false, and insertion index
        return (False, left)
    def add(self, key: int) -> None:
        if not self.hashSet:
            self.hashSet.append(key)
            return
        search_res = self.binary_search(self.hashSet, key)
        if search_res[0]:
            return
        self.hashSet.insert(search_res[1], key)
    def remove(self, key: int) -> None:
        if not self.hashSet:
            return 
        search_res = self.binary_search(self.hashSet, key)
        if not search_res[0]:
            return
        self.hashSet.pop(search_res[1])
    def contains(self, key: int) -> bool:
        if not self.hashSet:
            return False
        search_res = self.binary_search(self.hashSet, key)
        return search_res[0]

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)