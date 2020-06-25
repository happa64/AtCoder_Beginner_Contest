# https://atcoder.jp/contests/arc040/submissions/14670067
# A - 床塗り
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    r, b = 0, 0
    for _ in range(n):
        s = input()
        r += s.count("R")
        b += s.count("B")
    print("TAKAHASHI" if r > b else "AOKI" if b > r else "DRAW")


if __name__ == '__main__':
    resolve()
