# https://atcoder.jp/contests/abc032/submissions/17409063
# D - ナップサック問題
import sys
from itertools import product
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(N)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, left, right):
        """
        [left, right)のsegfuncしたものを得る
        left: index(0-index)
        right: index(0-index)
        """
        res = self.ide_ele
        left += self.num
        right += self.num
        while left < right:
            if left & 1:
                res = self.segfunc(res, self.tree[left])
                left += 1
            if right & 1:
                res = self.segfunc(res, self.tree[right - 1])
            left >>= 1
            right >>= 1
        return res


def resolve():
    N, W = map(int, input().split())
    VW = [list(map(int, input().split())) for _ in range(N)]

    if N <= 30:
        s = N // 2
        S = VW[:s]
        kouho_s = []
        for pattern in product([0, 1], repeat=s):
            sum_v, sum_w = 0, 0
            for idx, p in enumerate(pattern):
                if p == 1:
                    sum_v += S[idx][0]
                    sum_w += S[idx][1]
            kouho_s.append((sum_w, sum_v))

        t = N - s
        T = VW[s:]
        kouho_t = []
        for pattern in product([0, 1], repeat=t):
            sum_v, sum_w = 0, 0
            for idx, p in enumerate(pattern):
                if p == 1:
                    sum_v += T[idx][0]
                    sum_w += T[idx][1]
            kouho_t.append((sum_w, sum_v))

        kouho_t.sort(key=lambda x: x[0])
        kouho_tw = [w for w, _ in kouho_t]
        seg = SegTree([v for _, v in kouho_t], lambda x, y: max(x, y), -f_inf)

        res = 0
        for w, v in kouho_s:
            if W < w:
                continue
            lim = bisect_right(kouho_tw, W - w)
            max_v = seg.query(0, lim)
            tot = v + max_v
            res = max(res, tot)
        print(res)
    elif max([w for _, w in VW]) <= 1000:
        MAX_W = min(sum([w for _, w in VW]), W) + 1
        dp = [[0] * MAX_W for _ in range(N + 1)]
        for i in range(1, N + 1):
            v, w = VW[i - 1]
            for j in range(MAX_W):
                dp[i][j] = dp[i - 1][j]
                if j - w >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
        print(dp[-1][-1])
    elif max([v for v, _ in VW]) <= 1000:
        MAX_V = sum([v for v, _ in VW]) + 1
        dp = [[f_inf] * MAX_V for _ in range(N + 1)]
        dp[0][0] = 0
        for i in range(1, N + 1):
            v, w = VW[i - 1]
            for j in range(MAX_V):
                dp[i][j] = dp[i - 1][j]
                if j - v >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - v] + w)

        for i in reversed(range(MAX_V)):
            if dp[-1][i] <= W:
                print(i)
                break


if __name__ == '__main__':
    resolve()
