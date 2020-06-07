# https://atcoder.jp/contests/abc020/submissions/14080083
# A - クイズ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    q = int(input())
    print("ABC" if q == 1 else "chokudai")


if __name__ == '__main__':
    resolve()
