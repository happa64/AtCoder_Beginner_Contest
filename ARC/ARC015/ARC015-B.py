# https://atcoder.jp/contests/arc015/submissions/14422723
# B - 真冬日？真夏日？
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    res = [0] * 6
    for _ in range(n):
        ma, mi = map(float, input().split())
        if 35 <= ma:
            res[0] += 1
        elif 30 <= ma < 35:
            res[1] += 1
        elif 25 <= ma < 30:
            res[2] += 1
        elif ma < 0:
            res[5] += 1

        if 25 <= mi:
            res[3] += 1

        if mi < 0 and 0 <= ma:
            res[4] += 1

    print(*res)


if __name__ == '__main__':
    resolve()
