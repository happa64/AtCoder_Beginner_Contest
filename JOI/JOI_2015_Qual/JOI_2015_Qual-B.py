# https://atcoder.jp/contests/joi2015yo/submissions/16057513
# B - クリスマスパーティー (Christmas Party)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    m = int(input())
    A = list(map(int, input().split()))
    B = [list(map(int, input().split())) for _ in range(m)]

    res = [0] * n
    for i in range(m):
        target = A[i]
        cnt = 0
        for j in range(n):
            if B[i][j] == target:
                res[j] += 1
                cnt += 1
        res[target - 1] += n - cnt
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
