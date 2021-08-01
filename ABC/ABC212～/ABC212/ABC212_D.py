# https://atcoder.jp/contests/abc212/submissions/24704798
# D - Querying Multiset
import sys
from heapq import *

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    q = int(input())
    s = 0
    que = []
    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            x = int(query[1])
            heappush(que, x - s)
        elif query[0] == "2":
            x = int(query[1])
            s += x
        else:
            x = heappop(que)
            x += s
            print(x)


if __name__ == '__main__':
    solve()
