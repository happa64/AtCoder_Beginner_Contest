# https://atcoder.jp/contests/past202010-open/submissions/18010772
# K - 転倒数
import sys
from collections import Counter, defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9


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
    k = int(input())
    cnt = []
    B = [0] * k
    for i in range(k):
        n = int(input())
        A = list(map(int, input().split()))
        bit = BIT(21)
        for j in range(n):
            t = bit.sec_sum(A[j] + 1, 21)
            bit.update(A[j], 1)
            B[i] += t
        cnt.append(Counter(A))

    res = 0
    q = int(input())
    query = list(map(lambda x: int(x) - 1, input().split()))
    num_cnt = defaultdict(int)
    for b in query:
        res += B[b]
        res %= mod
        for i in range(1, 21):
            x = num_cnt[i]
            for j in range(1, i):
                y = cnt[b][j]
                res += (x * y) % mod
                res %= mod
        for i in range(1, 21):
            num_cnt[i] += cnt[b][i]
    print(res % mod)


if __name__ == '__main__':
    resolve()
