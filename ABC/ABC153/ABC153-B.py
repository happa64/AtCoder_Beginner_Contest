# https://atcoder.jp/contests/abc153/submissions/14270772
# B - Common Raccoon vs Monster
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    h, n = map(int, input().split())
    A = list(map(int, input().split()))

    print("Yes" if h <= sum(A) else "No")


if __name__ == '__main__':
    resolve()
