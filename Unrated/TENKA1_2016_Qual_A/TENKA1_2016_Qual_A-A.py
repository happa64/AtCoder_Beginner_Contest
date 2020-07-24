# https://atcoder.jp/contests/tenka1-2016-quala/submissions/15395277
# A - 天下一プログラマーゲーム
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    res = 0
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            continue
        else:
            res += i
    print(res)


if __name__ == '__main__':
    resolve()
