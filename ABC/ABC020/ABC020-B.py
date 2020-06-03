# https://atcoder.jp/contests/abc020/submissions/13970381
# B - 足し算
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = input().split()
    res = int(a + b) * 2
    print(res)


if __name__ == '__main__':
    resolve()
