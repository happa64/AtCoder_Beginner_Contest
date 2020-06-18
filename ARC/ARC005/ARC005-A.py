# https://atcoder.jp/contests/arc005/submissions/14446119
# A - 大好き高橋君
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    W = list(input().rstrip(".").split())
    L = ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]

    res = 0
    for w in W:
        if w in L:
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
