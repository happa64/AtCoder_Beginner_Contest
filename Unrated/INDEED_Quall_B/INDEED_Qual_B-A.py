# https://atcoder.jp/contests/indeednow-qualb/submissions/14386219
# A - 高橋くんとマンハッタン
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    res = abs(x1 - x2) + abs(y1 - y2) + 1
    print(res)


if __name__ == '__main__':
    resolve()
