# https://atcoder.jp/contests/keyence2019/submissions/13654934
# A - Beginning
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = list(map(int, input().split()))
    print("YES" if 1 in N and 9 in N and 7 in N and 4 in N else "NO")


if __name__ == '__main__':
    resolve()
