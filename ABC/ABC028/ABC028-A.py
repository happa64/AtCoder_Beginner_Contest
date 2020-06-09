# https://atcoder.jp/contests/abc028/submissions/14127315
# A - テスト評価
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    if n == 100:
        print("Perfect")
    elif 90 <= n <= 99:
        print("Great")
    elif 60 <= n <= 89:
        print("Good")
    else:
        print("Bad")


if __name__ == '__main__':
    resolve()
