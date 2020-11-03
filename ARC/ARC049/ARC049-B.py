# https://atcoder.jp/contests/arc049/submissions/15559759
# B - 高橋ノルム君
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """二分探索"""
    def meguru_bisect(ok, ng):
        while abs(ok - ng) > 10 ** -6:
            mid = (ok + ng) / 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(z):
        for i in range(n):
            for j in range(i + 1, n):
                dy = abs(Y[i] - Y[j])
                if dy > z / C[i] + z / C[j]:
                    return False
                dx = abs(X[i] - X[j])
                if dx > z / C[i] + z / C[j]:
                    return False
        return True

    n = int(input())
    X, Y, C = [], [], []
    for _ in range(n):
        x, y, c = map(int, input().split())
        X.append(x)
        Y.append(y)
        C.append(c)

    ng, ok = -1, 10 ** 8 + 1
    res = meguru_bisect(ok, ng)
    print(res)


def resolve2():
    """三分探索"""

    def ternary_search(x):
        high, low = -10 ** 5, 10 ** 5
        for _ in range(100):
            mid_left = high / 3 + low * 2 / 3
            mid_right = high * 2 / 3 + low / 3
            if f(x, mid_left) >= f(x, mid_right):
                low = mid_left
            else:
                high = mid_right
        return f(x, high)

    def f(x1, y1):
        res = 0
        for x2, y2, c in XYC:
            cost = c * max(abs(x1 - x2), abs(y1 - y2))
            res = max(res, cost)
        return res

    n = int(input())
    XYC = [list(map(int, input().split())) for _ in range(n)]

    high, low = -10 ** 5, 10 ** 5
    for _ in range(100):
        mid_left = high / 3 + low * 2 / 3
        mid_right = high * 2 / 3 + low / 3
        if ternary_search(mid_left) >= ternary_search(mid_right):
            low = mid_left
        else:
            high = mid_right

    print(ternary_search(high))


if __name__ == '__main__':
    resolve()
