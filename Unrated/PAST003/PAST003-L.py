# https://atcoder.jp/contests/past202005-open/submissions/18109233
# L - スーパーマーケット
import sys
from collections import deque, defaultdict

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
    def f(max_num, flg):
        print(max_num)
        idx = D[max_num]
        if flg:
            rm = seg2.query(idx, idx + 1)
            seg1.update(idx, rm)
        seg2.update(idx, goods[idx].popleft())

    n = int(input())
    goods = []
    for _ in range(n):
        _, *T = map(int, input().split())
        goods.append(deque(T + [0, 0]))
    m = int(input())
    A = list(map(int, input().split()))

    D = defaultdict(int)
    for i in range(n):
        for j in range(len(goods[i])):
            D[goods[i][j]] = i

    seg1 = SegTree([0] * n, lambda x, y: max(x, y), -f_inf)
    seg2 = SegTree([0] * n, lambda x, y: max(x, y), -f_inf)
    for i in range(n):
        seg1.update(i, goods[i].popleft())
        seg2.update(i, goods[i].popleft())

    for a in A:
        if a == 1:
            ma = seg1.query(0, n)
            f(ma, True)
        else:
            ma1 = seg1.query(0, n)
            ma2 = seg2.query(0, n)
            f(max(ma1, ma2), ma1 > ma2)


if __name__ == '__main__':
    resolve()
