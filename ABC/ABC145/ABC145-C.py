# https://atcoder.jp/contests/abc145/submissions/13597141
# C - Average Length
import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    def calc(x1, y1, x2, y2):
        return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)

    dist = 0
    cnt = 0
    for pattern in permutations(list(range(n))):
        cnt += 1
        for i in range(1, n):
            x1, y1 = XY[pattern[i - 1]]
            x2, y2 = XY[pattern[i]]
            dist += calc(x1, y1, x2, y2)

    print(dist / cnt)


if __name__ == '__main__':
    resolve()
