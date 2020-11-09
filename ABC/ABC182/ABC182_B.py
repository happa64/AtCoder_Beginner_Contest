# https://atcoder.jp/contests/abc182/submissions/17953235
# B - Almost GCD
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = -1
    ma = 0
    for i in range(2, 1001):
        cnt = 0
        for a in A:
            if a % i == 0:
                cnt += 1
        if ma < cnt:
            res = i
            ma = cnt
    print(res)


if __name__ == '__main__':
    resolve()
