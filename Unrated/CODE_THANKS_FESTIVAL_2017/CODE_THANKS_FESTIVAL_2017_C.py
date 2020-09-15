import sys
from heapq import heappush, heappop, heapify

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]
    heapify(AB)
    res = 0
    for _ in range(k):
        a, b = heappop(AB)
        res += a
        heappush(AB, [a + b, b])
    print(res)


if __name__ == '__main__':
    resolve()
