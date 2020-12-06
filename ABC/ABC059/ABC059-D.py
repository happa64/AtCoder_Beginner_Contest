# https://atcoder.jp/contests/abc059/submissions/18614342
# D - Alice&Brown
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())
    print("Alice" if abs(x - y) > 1 else "Brown")


if __name__ == '__main__':
    resolve()
