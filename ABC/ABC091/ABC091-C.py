# https://atcoder.jp/contests/arc092/submissions/13929247
# C - 2D Plane 2N Points
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0],
                reverse=True)
    CD = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

    res = 0
    for i in range(n):
        a, b = AB[i]
        for j in range(len(CD)):
            c, d = CD[j]
            if a < c and b < d:
                res += 1
                CD.pop(j)
                break

    print(res)


if __name__ == '__main__':
    resolve()
