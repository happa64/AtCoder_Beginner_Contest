# https://atcoder.jp/contests/past202012-open/submissions/19042590
# C - 三十六進法
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = ""
    for i in reversed(range(5)):
        q, n = divmod(n, pow(36, i))
        if q == 0 and len(res) == 0:
            continue

        if q <= 9:
            res += str(q)
        else:
            res += chr(ord("A") + q - 10)

    print(res if len(res) else 0)


if __name__ == '__main__':
    resolve()
