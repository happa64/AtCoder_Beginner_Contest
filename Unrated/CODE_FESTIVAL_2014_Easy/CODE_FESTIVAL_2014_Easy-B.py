# https://atcoder.jp/contests/code-festival-2014-morning-easy/submissions/14914231
# B - チーム作り
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    n -= 1
    q, r = divmod(n, 20)

    print(r + 1 if q % 2 == 0 else 20 - r)


if __name__ == '__main__':
    resolve()
