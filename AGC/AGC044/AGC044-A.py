# https://atcoder.jp/contests/agc044/submissions/13556795
# A - Pay to Win
import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def solve(N, A, B, C, D):

        # Nを0にするために必要なコインをメモ化再帰で求める
        @lru_cache(None)
        def f(N):
            # 再帰終了条件
            if N == 0:
                return 0
            if N == 1:
                return D

            ret = D * N

            q, r = divmod(N, 2)
            # Nが2で割り切れる場合、必要な追加コインはA枚
            if r == 0:
                ret = min(ret, f(q) + A)
            # Nが2で割り切れない場合、必要な追加コインはA+D枚
            else:
                # f(q) + A + D：qを2倍した後に1を足す
                # f(q + 1) + A + D：q+1を2倍した後に1を引く
                ret = min(ret, f(q) + A + D, f(q + 1) + A + D)

            q, r = divmod(N, 3)
            # Nが3で割り切れる場合、必要な追加コインはB枚
            if r == 0:
                ret = min(ret, f(q) + B)
            # Nが3で割った余りが1の時、qを3倍して1を足すのが、最もコインが少なくて済む為、必要な追加コインはB+D枚
            elif r == 1:
                ret = min(ret, f(q) + B + D)
            # Nが3で割った余りが2の時、q+1を3倍した後に1を引くのが、最もコインが少なくて済む為、必要な追加コインはB+D枚
            else:
                ret = min(ret, f(q + 1) + B + D)

            q, r = divmod(N, 5)
            # Nが5で割り切れる場合、必要な追加コインはC枚
            if r == 0:
                ret = min(ret, f(q) + C)
            # Nが5で割った余りが1の時、qを5倍して1を足すのが、最もコインが少なくて済む為、必要な追加コインはC+D枚
            elif r == 1:
                ret = min(ret, f(q) + C + D)
            # Nが5で割った余りが2の時、qを5倍して2を足すのが、最もコインが少なくて済む為、必要な追加コインはC+2D枚
            elif r == 2:
                ret = min(ret, f(q) + C + D + D)
            # Nが5で割った余りが3の時、q+1を5倍して2を引くのが、最もコインが少なくて済む為、必要な追加コインはC+2D枚
            elif r == 3:
                ret = min(ret, f(q + 1) + C + D + D)
            # Nが5で割った余りが3の時、q+1を5倍して1を引くのが、最もコインが少なくて済む為、必要な追加コインはC+D枚
            else:
                ret = min(ret, f(q + 1) + C + D)

            return ret

        return f(N)

    t = int(input())
    for _ in range(t):
        n, a, b, c, d = map(int, input().split())
        print(solve(n, a, b, c, d))


if __name__ == '__main__':
    resolve()
