# https://atcoder.jp/contests/abc016/submissions/14079858
# A - 12月6日
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    M, D = map(int, input().split())
    print("YES" if M % D == 0 else "NO")


if __name__ == '__main__':
    resolve()
