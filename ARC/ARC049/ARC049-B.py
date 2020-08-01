# https://atcoder.jp/contests/arc049/submissions/15559759
# B - 高橋ノルム君
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
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


if __name__ == '__main__':
    resolve()
