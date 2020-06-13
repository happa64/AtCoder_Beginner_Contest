# https://atcoder.jp/contests/abc054/submissions/14206629
# A - One Card Poker
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    L = list(range(2, 14)) + [1]
    idx_a = L.index(a)
    idx_b = L.index(b)
    if idx_a == idx_b:
        print("Draw")
    elif idx_a < idx_b:
        print("Bob")
    else:
        print("Alice")


if __name__ == '__main__':
    resolve()
