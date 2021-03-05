from heapq import heappush, heappop


class MultiSet:
    def __init__(self):
        self.q = []
        self.deleted = []

    def len(self):
        """ 集合の長さを返す """
        return len(self.q) - len(self.deleted)

    def get_min(self):
        """ 集合の最小値を返す。O(logN) """
        while len(self.q) > 0 and len(self.deleted) and self.q[0] == self.deleted[0]:
            heappop(self.q)
            heappop(self.deleted)
        return self.q[0] if len(self.q) > 0 else None

    def insert(self, v):
        """ 集合の最小値を返すと共に、集合に値を挿入する。O(logN) """
        ret = self.get_min()
        heappush(self.q, v)
        return ret

    def delete(self, v):
        """ 集合の最小値を返すと共に、集合から値を削除する。O(logN) """
        ret = self.get_min()
        heappush(self.deleted, v)
        return ret

    def __str__(self):
        return str(self.q) + " " + str(self.deleted)