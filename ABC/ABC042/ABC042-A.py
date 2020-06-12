# https://atcoder.jp/contests/abc042/submissions/14186314
# A - 和風いろはちゃんイージー
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ABC = list(input().split())
    print("YES" if ABC.count("5") == 2 and ABC.count("7") == 1 else "NO")


if __name__ == '__main__':
    resolve()
