# https://atcoder.jp/contests/abc128/submissions/20666997
# E - Roadwork
import sys
from heapq import heappush, heappop

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


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


def resolve():
    n, q = map(int, input().split())
    event = []
    for _ in range(n):
        s, t, x = map(int, input().split())
        event.append((s - x, x))
        event.append((t - x, -x))
    n = len(event)
    event.sort()
    D = list(int(input()) for _ in range(q))

    res = [0] * q
    multiset = MultiSet()
    j = 0
    for i, d in enumerate(D):
        while j < n and event[j][0] <= d:
            _, x = event[j]
            multiset.insert(x) if x >= 0 else multiset.delete(-x)
            j += 1
        mi = multiset.get_min()
        res[i] = mi if mi is not None else -1
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
