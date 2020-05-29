import sys
from itertools import product, combinations
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n - 1)]
    ans = -float('inf')

    # 3^N組み合わせを列挙
    for pattern in product([0, 1, 2], repeat=n):
        g1, g2, g3 = [], [], []
        for idx, key in enumerate(pattern):
            if key == 0:
                g1.append(idx)
            elif key == 1:
                g2.append(idx)
            else:
                g3.append(idx)

        # 各組み合わせの合計幸福度を計算し、その最大値を返す
        A = 0
        for g in [g1, g2, g3]:
            for i, j in combinations(g, 2):
                A += a[i][j - i - 1]
        ans = max(ans, A)

    print(ans)


if __name__ == '__main__':
    resolve()
