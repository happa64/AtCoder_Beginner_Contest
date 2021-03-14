# https://atcoder.jp/contests/abc195/submissions/20890815
# D - Shipping Center
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, m, q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(n)]
    WV.sort(key=lambda x: [-x[1], x[0]])
    X = list(map(int, input().split()))

    for _ in range(q):
        l, r = map(int, input().split())
        can_use_x = X[:l - 1] + X[r:]
        can_use_x.sort()
        res = 0
        used_idx = set()
        for w, v in WV:
            for i in range(len(can_use_x)):
                if i not in used_idx and can_use_x[i] >= w:
                    used_idx.add(i)
                    res += v
                    break
        print(res)


if __name__ == '__main__':
    solve()
