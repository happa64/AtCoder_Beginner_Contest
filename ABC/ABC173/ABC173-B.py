# https://atcoder.jp/contests/abc173/submissions/14973521
# B - Judge Status Summary
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = list(input() for _ in range(n))
    AC = S.count("AC")
    WA = S.count("WA")
    TLE = S.count("TLE")
    RE = S.count("RE")

    print("AC", "x", AC)
    print("WA", "x", WA)
    print("TLE", "x", TLE)
    print("RE", "x", RE)


if __name__ == '__main__':
    resolve()
