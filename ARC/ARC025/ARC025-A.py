# https://atcoder.jp/contests/arc025/submissions/14638144
# A - ゴールドラッシュ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    D = list(map(int, input().split()))
    J = list(map(int, input().split()))

    res = 0
    for i in range(7):
        res += max(D[i], J[i])
    print(res)


if __name__ == '__main__':
    resolve()
