# https://atcoder.jp/contests/abc152/submissions/13689741
# D - Handstand 2
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    res = 0
    numbers = [[0] * 10 for _ in range(10)]
    for i in range(1, n + 1):
        ss = str(i)
        numbers[int(ss[0])][int(ss[-1])] += 1

    for j in range(1, 10):
        for k in range(1, 10):
            res += numbers[j][k] * numbers[k][j]

    print(res)


if __name__ == '__main__':
    resolve()
