# https://atcoder.jp/contests/joi2020yo2/submissions/16999050
# B - いちご (Strawberry)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AT = [list(map(int, input().split())) for _ in range(n)]
    AT.sort(key=lambda x: x[0], reverse=True)

    res = AT[0][0]
    now_pos = now_time = AT[0][0]
    for a, t in AT:
        res += now_pos - a
        now_time += now_pos - a
        if now_time < t:
            res += t - now_time
            now_time = t
        now_pos = a
    res += AT[-1][0]

    print(res)


if __name__ == '__main__':
    resolve()
