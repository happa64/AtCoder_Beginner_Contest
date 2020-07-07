# https://atcoder.jp/contests/joi2012yo/submissions/15056803
# B - サッカー (Soccer)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    point = [0] * n
    for _ in range((n * (n - 1)) // 2):
        a, b, c, d = map(int, input().split())
        if c > d:
            point[a - 1] += 3
        elif c < d:
            point[b - 1] += 3
        else:
            point[a - 1] += 1
            point[b - 1] += 1

    score = []
    for idx, p in enumerate(point):
        score.append([idx, p])
    score.sort(key=lambda x: -x[1])

    res = [0] * n
    for i in range(n):
        if i == 0:
            idx, _ = score[i]
            res[idx] = i + 1
        else:
            prev_idx, prev = score[i - 1]
            idx, p = score[i]
            res[idx] = res[prev_idx] if prev == p else i + 1
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
