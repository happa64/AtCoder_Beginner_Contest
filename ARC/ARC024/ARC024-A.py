# https://atcoder.jp/contests/arc024/submissions/14638080
# A - くつがくっつく
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    l, r = map(int, input().split())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))

    res = 0
    used = [0] * r
    for i in range(l):
        for j in range(r):
            if L[i] == R[j] and not used[j]:
                res += 1
                used[j] = True
                break
    print(res)


if __name__ == '__main__':
    resolve()
