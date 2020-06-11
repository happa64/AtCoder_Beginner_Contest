# https://atcoder.jp/contests/abc039/submissions/14167887
# A - 高橋直体
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    res = a * b + b * c + c * a
    print(res * 2)


if __name__ == '__main__':
    resolve()
