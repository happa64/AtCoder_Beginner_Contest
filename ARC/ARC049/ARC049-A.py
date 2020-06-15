# https://atcoder.jp/contests/arc049/submissions/14378935
# A - "強調"
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = list(input())
    a, b, c, d = map(int, input().split())
    cnt = 0
    for i in [a, b, c, d]:
        s.insert(i + cnt, "\"")
        cnt += 1
    print("".join(s))


if __name__ == '__main__':
    resolve()
