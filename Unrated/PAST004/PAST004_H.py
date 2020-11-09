# https://atcoder.jp/contests/past202010-open/submissions/18010719
# H - マス目のカット
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, k = map(int, input().split())
    S = [list(input().rstrip()) for _ in range(H)]

    ruiseki = [[] for _ in range(10)]
    for num in range(10):
        D = [[0] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if int(S[i][j]) == num:
                    D[i][j] = 1

        R = [[0] * (W + 1) for _ in range(H + 1)]
        for i in range(H):
            for j in range(W):
                R[i + 1][j + 1] = R[i][j + 1] + R[i + 1][j] - R[i][j] + D[i][j]
        ruiseki[num] = R

    res = 0
    for y1 in range(H):
        for x1 in range(W):
            for n in range(1, 31):
                y2, x2 = y1 + n, x1 + n
                if y2 > H or x2 > W:
                    continue
                area = (x2 - x1) * (y2 - y1)
                nums = [0] * 10
                for num in range(10):
                    R = ruiseki[num]
                    cnt = R[y2][x2] - R[y1][x2] - R[y2][x1] + R[y1][x1]
                    nums[num] = cnt
                ma = max(nums)
                diff = area - ma
                if diff <= k:
                    res = max(res, n)
    print(res)


if __name__ == '__main__':
    resolve()
