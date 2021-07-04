# https://atcoder.jp/contests/typical90/submissions/23945062
# 017 - Crossing Segments（★7）
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


class BIT:
    """ 1-indexで使用しないと無限ループするので注意 """

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, x):
        """ idx番目にxをO(logN)で加算する """
        while idx <= self.n:
            self.bit[idx] += x
            idx += idx & (-idx)

    def query(self, idx):
        """ 1 ~ idx番目までの区間和をO(logN)で返す """
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & (-idx)
        return res

    def sec_sum(self, left, right):
        """ left ~ right番目までの区間和をO(logN)で返す """
        return self.query(right) - self.query(left)

    def lower_bound(self, w):
        """ 区間和がw以上になる最小のindexをO(logN)で返す """
        if w <= 0:
            return 0
        x = 0
        k = 1 << self.n.bit_length()
        while k:
            if x + k <= self.n and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x + 1

    def debug(self):
        """ bitの状態を出力する """
        print(*[self.sec_sum(i, i) for i in range(1, self.n + 1)])


def solve():
    n, m = map(int, input().split())
    LR = [tuple(map(int, input().split())) for _ in range(m)]
    LR.sort(key=lambda x: [x[1], x[0]])

    V3 = [0] * (n + 1)
    for l, r in LR:
        V3[l] += 1
        V3[r] += 1
    ans1 = sum(V3[i] * (V3[i] - 1) // 2 for i in range(1, n + 1))

    V1, V2 = [0] * (n + 1), [0] * (n + 1)
    for l, r in LR:
        V1[r] += 1
        V2[l - 1] += 1
    V1 = tuple(accumulate(V1))
    ans2 = sum(V1[i] * V2[i] for i in range(1, n + 1))

    ans3 = 0
    bit = BIT(n + 2)
    for l, r in LR:
        cnt = bit.sec_sum(l, r)
        ans3 += cnt
        bit.update(l, 1)

    res = m * (m - 1) // 2 - ans1 - ans2 - ans3
    print(res)


if __name__ == '__main__':
    solve()
