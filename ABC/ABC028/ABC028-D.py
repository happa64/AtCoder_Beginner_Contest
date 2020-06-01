# https://atcoder.jp/contests/abc028/submissions/13146873
# D - 乱数生成
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    total = pow(n, 3)

    # (kより小さい数，k，kより大きい数)＊3!
    p1 = (k - 1) * (n - k) * 6

    # (kより小さい数，k，k)＊3C2
    p2 = (k - 1) * 3

    # (k，k，kより大きい数)＊3C2
    p3 = (n - k) * 3

    # p1+p2+p3+(k,k,k)の場合
    p = p1 + p2 + p3 + 1

    print(p / total)


if __name__ == '__main__':
    resolve()
