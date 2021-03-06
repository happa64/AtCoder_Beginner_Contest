# https://atcoder.jp/contests/nikkei2019-final/submissions/17895142
# C - Come Together
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def ternary_search(left, right, l, L):
        for _ in range(30):
            mid_right = (left * 2 + right) // 3
            mid_left = (left + right * 2) // 3
            if f(mid_right, l, L) < f(mid_left, l, L):
                right = mid_left
            else:
                left = mid_right

        mi = f_inf
        for i in range(left, right + 1):
            mi = min(mi, f(i, l, L))

        return mi

    def f(x, l, cnt):
        ret = 0
        for i in range(1, l + 1):
            ret += abs(x - i) * cnt[i - 1]
        return ret

    h, w, k = map(int, input().split())

    C = [h] * w
    R = [w] * h
    for _ in range(k):
        r, c = map(lambda x: int(x) - 1, input().split())
        R[r] -= 1
        C[c] -= 1

    res = ternary_search(0, h, h, R) + ternary_search(0, w, w, C)
    print(res)


if __name__ == '__main__':
    resolve()
