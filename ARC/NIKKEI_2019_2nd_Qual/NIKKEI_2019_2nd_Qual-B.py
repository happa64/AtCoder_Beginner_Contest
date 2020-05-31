# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_b
# B - Counting of Trees
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 998244353


def resolve():
    n = int(input())
    D = list(map(int, input().split()))

    tree = [0 for _ in range(max(D) + 1)]
    for i in range(n):
        idx = D[i]
        tree[idx] += 1

    if D[0] != 0 or tree[0] != 1 or 0 in tree:
        print(0)
        exit()

    res = 1
    for i in range(len(tree) - 1):
        res *= pow(tree[i], tree[i + 1], mod)

    print(res % mod)


if __name__ == '__main__':
    resolve()
