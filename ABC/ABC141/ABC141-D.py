# https://atcoder.jp/contests/abc141/submissions/14430277
# D - Powerful Discount Tickets
import sys
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(lambda x: int(x) * (-1), input().split()))
    heapify(A)
    for _ in range(m):
        a = (heappop(A) * (-1)) // 2
        heappush(A, a * (-1))

    print(sum(A) * (-1))


if __name__ == '__main__':
    resolve()
