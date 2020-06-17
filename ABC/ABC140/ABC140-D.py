# https://atcoder.jp/contests/abc140/submissions/14432484
# D - Face Produces Unhappiness
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    S = input().strip()

    cnt = 0
    for i in range(1, n):
        if S[i - 1] == S[i]:
            cnt += 1

    res = min(cnt + k * 2, n - 1)
    print(res)


def resolve2():
    n, k = map(int, input().split())
    S = input().strip()

    score = 0
    diff = 0
    for i in range(1, n):
        if S[i - 1] == S[i]:
            score += 1
        else:
            diff += 1

    print(min(score + min(diff, k) * 2, n - 1))


if __name__ == '__main__':
    resolve2()
