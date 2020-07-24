# https://atcoder.jp/contests/tenka1-2016-qualb/submissions/15395334
# A - 天下一合成関数
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def f(x):
        return (x ** 2 + 4) // 8

    print(f(f(f(20))))


if __name__ == '__main__':
    resolve()
