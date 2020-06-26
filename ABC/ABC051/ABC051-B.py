# https://atcoder.jp/contests/abc051/submissions/12823655
# B - Sum of Three Integers
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k, s = map(int, input().split())

    res = 0
    for x in range(k + 1):
        for y in range(k + 1):
            z = s - x - y
            if x + y + z == s and k >= z >= 0:
                res += 1

    print(res)


if __name__ == '__main__':
    resolve()
