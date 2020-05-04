# https://atcoder.jp/contests/abc166/tasks/abc166_c
# C - Peaks
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    H = list(map(int, input().split()))

    tree = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    res = 0
    for i in range(n):
        A = H[i]
        if len(tree[i]) >= 1:
            for j in tree[i]:
                B = H[j]
                if A <= B:
                    break
            else:
                res += 1
        else:
            res += 1

    print(res)


if __name__ == '__main__':
    resolve()
