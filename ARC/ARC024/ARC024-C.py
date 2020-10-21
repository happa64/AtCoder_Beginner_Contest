# https://atcoder.jp/contests/arc024/submissions/17558108
# C - だれじゃ
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N, K = map(int, input().split())
    S = input()

    cnt = [[0] * N for _ in range(26)]
    for i in range(N):
        idx = ord(S[i]) - ord("a")
        cnt[idx][i] += 1

    cnt_acc = [[] for _ in range(26)]
    for i in range(26):
        cnt_acc[i] = [0] + list(accumulate(cnt[i]))

    res = [[] for _ in range(N - K + 1)]
    for i in range(N - K + 1):
        left = i
        right = i + K
        tmp = [0] * 26
        for j in range(26):
            cnt_s = cnt_acc[j][right] - cnt_acc[j][left]
            tmp[j] = cnt_s
        res[i] = [tmp, i]
    res.sort()

    i = j = 0
    while i < N - K + 1:
        while i < N - K + 1 and j < N - K + 1 and res[i][0] == res[j][0]:
            left, right = res[i][1], res[j][1]
            if abs(right - left) >= K:
                print("YES")
                exit()
            else:
                j += 1
        i = j
    print("NO")


if __name__ == '__main__':
    resolve()
