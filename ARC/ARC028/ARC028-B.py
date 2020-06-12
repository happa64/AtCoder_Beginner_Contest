# https://atcoder.jp/contests/arc028/submissions/14192508
# B - 特別賞
import sys
from heapq import heapreplace, heappush

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))

    que = []
    for i in range(k):
        heappush(que, [-x[i], i + 1])

    kth_age, Rank = que[0]
    print(Rank)
    kth_age *= -1

    for i in range(k, n):
        if x[i] < kth_age:
            heapreplace(que, [-x[i], i + 1])
            kth_age, Rank = que[0]
            print(Rank)
            kth_age *= -1
        else:
            _, Rank = que[0]
            print(Rank)


if __name__ == '__main__':
    resolve()
