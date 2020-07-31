# https://atcoder.jp/contests/arc045/tasks/arc045_b
# B - ドキドキデート大作戦高橋君
import sys
from itertools import accumulate

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


def segfunc(x, y):
    """
    区間(x,y)に対して行いたい操作の入力
    最小値：min(x,y)
    最大値：max(x,y)
    和：x + y
    積：x * y
    最大公約数：math.gcd(x, y)
    """
    return min(x, y)


# 単位元の入力
ide_ele = f_inf


def resolve():
    n, m = map(int, input().split())
    imos = [0] * (n + 1)
    ST = []
    for _ in range(m):
        s, t = map(lambda x: int(x) - 1, input().split())
        ST.append([s, t])
        imos[s] += 1
        imos[t + 1] -= 1

    sec_cnt = list(accumulate(imos))[:n]
    seg = SegTree(sec_cnt, segfunc, ide_ele)
    res = []
    for i in range(m):
        s, t = ST[i]
        if seg.query(s, t + 1) != 1:
            res.append(i + 1)
    print(len(res))
    if len(res) != 0:
        print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
