# https://atcoder.jp/contests/agc032/submissions/14659315
# B - Balanced Neighbors
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = []
    c = n
    if n % 2 != 0:
        c -= 1

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if j == c:
                continue
            res.append([i, j])
        c -= 1

    print(len(res))
    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
