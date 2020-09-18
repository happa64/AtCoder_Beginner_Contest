# https://atcoder.jp/contests/ddcc2016-final/submissions/16820101
# A - 正方形のチップ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    r, c = map(int, input().split())

    res = 0
    for w in range(c, r, c):
        H = pow(pow(r, 2) - pow(w, 2), 0.5)
        res += int(H // c)
    print(res * 4)


if __name__ == '__main__':
    resolve()
