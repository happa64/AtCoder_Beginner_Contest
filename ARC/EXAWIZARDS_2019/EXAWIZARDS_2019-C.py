# https://atcoder.jp/contests/exawizards2019/submissions/19390390
# C - Snuke the Wizard
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def meguru_bisect_left(left, right):
        while abs(left - right) > 1:
            mid = (left + right) // 2
            if is_ok(mid) == -1:
                left = mid
            else:
                right = mid
        return right

    def meguru_bisect_right(left, right):
        while abs(left - right) > 1:
            mid = (left + right) // 2
            if is_ok(mid) == 1:
                right = mid
            else:
                left = mid
        return left

    def is_ok(pos):
        for t, d in query:
            if t == S[pos]:
                pos += -1 if d == "L" else 1
                if pos < 0:
                    return -1
                if pos >= n:
                    return 1
        return 0

    n, q = map(int, input().split())
    S = input().rstrip()
    query = [list(input().split()) for _ in range(q)]

    left_fall = meguru_bisect_left(-1, n)
    right_fall = n - 1 - meguru_bisect_right(-1, n)
    res = n - left_fall - right_fall
    print(res)


if __name__ == '__main__':
    resolve()
