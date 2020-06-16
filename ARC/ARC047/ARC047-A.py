# https://atcoder.jp/contests/arc047/submissions/14403188
# A - タブの開きすぎ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, l = map(int, input().split())
    S = input()

    cnt = 1
    res = 0
    for s in S:
        if s == "+":
            cnt += 1
        else:
            cnt -= 1
            cnt = max(cnt, 1)

        if cnt > l:
            res += 1
            cnt = 1

    print(res)


if __name__ == '__main__':
    resolve()
