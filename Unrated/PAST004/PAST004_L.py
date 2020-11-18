# https://atcoder.jp/contests/past202010-open/submissions/18201844
# L - マンションの改築
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q = map(int, input().split())
    H = [f_inf] + list(map(int, input().split())) + [f_inf]

    dict_diff_odd = defaultdict(int)
    dict_diff_even = defaultdict(int)
    for i in range(n + 1):
        if i % 2:
            dict_diff_odd[H[i] - H[i + 1]] += 1
        else:
            dict_diff_even[H[i] - H[i + 1]] += 1

    odd = even = 0
    for _ in range(q):
        t, *query = map(int, input().split())
        if t == 1:
            v = query[0]
            odd += v
            even -= v
        elif t == 2:
            v = query[0]
            odd -= v
            even += v
        else:
            u, v = query
            if u % 2 == 0:
                dict_diff_odd[H[u - 1] - H[u]] -= 1
                dict_diff_even[H[u] - H[u + 1]] -= 1
                H[u] += v
                dict_diff_odd[H[u - 1] - H[u]] += 1
                dict_diff_even[H[u] - H[u + 1]] += 1
            else:
                dict_diff_even[H[u - 1] - H[u]] -= 1
                dict_diff_odd[H[u] - H[u + 1]] -= 1
                H[u] += v
                dict_diff_even[H[u - 1] - H[u]] += 1
                dict_diff_odd[H[u] - H[u + 1]] += 1

        res = dict_diff_odd[-odd] + dict_diff_even[-even]
        print(res)


if __name__ == '__main__':
    resolve()
