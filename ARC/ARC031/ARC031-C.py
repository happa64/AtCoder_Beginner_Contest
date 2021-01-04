# https://atcoder.jp/contests/arc031/submissions/19202918
# C - 積み木
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


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
        return self.query(right) - self.query(left - 1)

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


def resolve():
    n = int(input())
    B = list(map(int, input().split()))
    que = [[B[i], i + 1] for i in range(n)]
    que.sort()

    bit = BIT(n)
    res = 0
    for _, idx in que:
        left = idx - bit.query(idx) - 1
        right = n - idx - bit.sec_sum(idx, n)
        if left < right:
            res += left
        else:
            res += right
        bit.update(idx, 1)
    print(res)


if __name__ == '__main__':
    resolve()
