# https://atcoder.jp/contests/agc010/submissions/13212989
# A - Addition
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    odd = 0
    for a in A:
        odd += 1 if a % 2 != 0 else 0

    print("YES") if odd % 2 == 0 else print("NO")


if __name__ == '__main__':
    resolve()
