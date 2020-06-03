# https://atcoder.jp/contests/agc014/submissions/12941524
# B - Unplanned Queries
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    cnt = [0] * n
    for i in range(m):
        a, b = map(int, input().split())
        cnt[a - 1] += 1
        cnt[b - 1] += 1

    for i in cnt:
        if i % 2:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    resolve()
