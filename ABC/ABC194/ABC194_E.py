# https://atcoder.jp/contests/abc194/submissions/20741877
# E - Mex Min
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


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


seg = SegTree([], lambda x, y: min(x, y), f_inf)


def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    res = [0] * (n - m + 1)
    seg = SegTree(list(range(n + 1)), lambda x, y: min(x, y), f_inf)
    cnt = defaultdict(int)
    for a in A[:m]:
        cnt[a] += 1
        seg.update(a, f_inf)
    res[0] = seg.query(0, n + 1)
    for i in range(n - m):
        l, r = A[i], A[i + m]
        cnt[l] -= 1
        if not cnt[l]:
            seg.update(l, l)
        cnt[r] += 1
        seg.update(r, f_inf)
        res[i + 1] = seg.query(0, n + 1)
    print(min(res))


if __name__ == '__main__':
    solve()
