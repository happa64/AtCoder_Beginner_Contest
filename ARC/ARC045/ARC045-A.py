# https://atcoder.jp/contests/arc045/submissions/14402817
# A - スペース高橋君
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = list(input().split())

    res = []
    for s in S:
        if s == "Left":
            res.append("<")
        elif s == "Right":
            res.append(">")
        else:
            res.append("A")
    print(*res)


if __name__ == '__main__':
    resolve()
