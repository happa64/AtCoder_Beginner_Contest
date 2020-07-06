# https://atcoder.jp/contests/joi2011yo/submissions/15049902
# A - 合計時間 (Total Time)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    res = 0
    for _ in range(4):
        res += int(input())
    print(res // 60)
    print(res % 60)


if __name__ == '__main__':
    resolve()
