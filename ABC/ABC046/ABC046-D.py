# https://atcoder.jp/contests/abc046/submissions/14211517
# D - AtCoDeerくんと変なじゃんけん
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()

    n = len(s) // 2
    p = s.count("p")
    print(n - p)


if __name__ == '__main__':
    resolve()
