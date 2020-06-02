# https://atcoder.jp/contests/abc014/submissions/13942263
# C - AtColor
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    MAX = 10 ** 6 + 2
    res = [0] * MAX
    for _ in range(n):
        a, b = map(int, input().split())
        res[a] += 1
        res[b + 1] -= 1

    for i in range(1, MAX):
        res[i] += res[i - 1]

    print(max(res))


if __name__ == '__main__':
    resolve()
