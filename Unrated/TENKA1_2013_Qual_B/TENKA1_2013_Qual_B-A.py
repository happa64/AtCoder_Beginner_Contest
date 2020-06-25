# https://atcoder.jp/contests/tenka1-2013-qualb/submissions/14670353
# A - 天下一人力比較
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = sorted(list(input() for _ in range(15)))
    print(S[6])


if __name__ == '__main__':
    resolve()
