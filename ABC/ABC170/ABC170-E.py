# https://atcoder.jp/contests/abc170/submissions/15403605
# E - Smart Infants
import sys
from heapq import heappop, heappush, heapify

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
MAX = 2 * 10 ** 5 + 1


def resolve():
    def max_rate_in_cls(c):
        """
        各幼稚園の最強園児のレートを返す
        所属している園児がいなければ0を返す
        :param c: 幼稚園児の所属
        """
        q = class_rate[c]
        while q:
            x, enj = q[0]
            # 園児の所属が最新と一致していれば、それが最強園児
            if enji_cls[enj] == c:
                return -x
            heappop(q)
        return 0

    def get_ans():
        q = max_rate
        while True:
            x, c = q[0]
            if max_rate_in_cls(c) == x:
                return x
            heappop(q)

    n, q = map(int, input().split())

    # 各園児のレート
    enji_rate = [0] * (n + 1)
    # 各園児の所属幼稚園
    enji_cls = [0] * (n + 1)
    # 各幼稚園のレート分布
    class_rate = [[] for _ in range(MAX)]
    for i in range(1, n + 1):
        rate, cls = map(int, input().split())
        enji_rate[i] = rate
        enji_cls[i] = cls
        heappush(class_rate[cls], (-rate, i))

    # 各クラスの最強園児のレート
    max_rate = []
    for c in range(MAX):
        x = max_rate_in_cls(c)
        if x:
            max_rate.append((x, c))
    heapify(max_rate)

    for _ in range(q):
        enj, after_cls = map(int, input().split())
        before_cls = enji_cls[enj]
        # 転園後の幼稚園に、転園前のデータを追加
        heappush(class_rate[after_cls], (-enji_rate[enj], enj))
        # 園児の所属幼稚園を更新
        enji_cls[enj] = after_cls
        for c in (before_cls, after_cls):
            x = max_rate_in_cls(c)
            if x != 0:
                heappush(max_rate, (x, c))
        print(get_ans())


if __name__ == '__main__':
    resolve()
