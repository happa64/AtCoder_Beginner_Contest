# https://atcoder.jp/contests/indeednow-quala/submissions/14799845
# B - Indeedなう！
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = sorted("indeednow")
    for _ in range(n):
        s = sorted(input())
        print("YES" if S == s else "NO")


if __name__ == '__main__':
    resolve()
