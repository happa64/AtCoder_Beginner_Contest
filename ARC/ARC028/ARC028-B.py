# https://atcoder.jp/contests/arc028/submissions/14695720
# B - 特別賞
import sys
from heapq import heappush, heapreplace
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    X = list(map(int, input().split()))

    rank = []
    for i in range(k):
        heappush(rank, [-X[i], i + 1])

    print(rank[0][1])
    for i in range(k, n):
        if X[i] < rank[0][0] * (-1):
            heapreplace(rank, [-X[i], i + 1])
            print(rank[0][1])
        else:
            print(rank[0][1])


if __name__ == '__main__':
    resolve()
