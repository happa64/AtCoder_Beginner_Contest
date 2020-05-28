# https://atcoder.jp/contests/past202004-open/submissions/13664393
# I - トーナメント
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    remain = []
    for i in range(1 << n):
        remain.append([i, A[i]])

    res = [0] * (1 << n)
    cnt = 1
    while len(remain) >= 1:
        if len(remain) == 1:
            res[remain[0][0]] = cnt - 1
            break

        tmp = []
        for i in range(0, len(remain), 2):
            x, y = remain[i][1], remain[i + 1][1]
            if x < y:
                tmp.append([remain[i + 1][0], y])
                res[remain[i][0]] = cnt
            else:
                tmp.append([remain[i][0], x])
                res[remain[i + 1][0]] = cnt

        remain = tmp
        cnt += 1

    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
