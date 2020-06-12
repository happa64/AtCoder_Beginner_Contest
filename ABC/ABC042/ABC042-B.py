# https://atcoder.jp/contests/abc042/submissions/12326156
# B - 文字列大好きいろはちゃんイージー
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, l = map(int, input().split())
    S = sorted(list(input() for _ in range(n)))
    print("".join(S))


if __name__ == '__main__':
    resolve()
