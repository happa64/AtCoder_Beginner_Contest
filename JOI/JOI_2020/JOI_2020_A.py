# https://atcoder.jp/contests/joi2020ho/submissions/17080412
# A - 長いだけのネクタイ (Just Long Neckties)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = sorted([[a, idx] for idx, a in enumerate(map(int, input().split()))])
    B = sorted(list(map(int, input().split())))

    diff_left = []
    diff_right = []
    for i in range(n):
        diff_left.append(max(A[i][0] - B[i], 0))
        diff_right.append(max(A[i + 1][0] - B[i], 0))

    max_left = [0]
    for i in range(n):
        max_left.append(diff_left[i] if max_left[-1] < diff_left[i] else max_left[-1])

    max_right = [0]
    for i in reversed(range(n)):
        max_right.append(diff_right[i] if max_right[-1] < diff_right[i] else max_right[-1])
    max_right = max_right[::-1]

    res = [0] * (n + 1)
    for i in range(n + 1):
        _, idx = A[i]
        res[idx] = max(max_left[i], max_right[i])
    print(*res)


if __name__ == '__main__':
    resolve()
