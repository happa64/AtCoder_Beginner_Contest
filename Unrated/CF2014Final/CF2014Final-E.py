# https://atcoder.jp/contests/code-festival-2014-final/submissions/13381855
# E - 常ならずグラフ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        常ならずグラフでは、始点と終点を除いた全ての点が、谷もしくは山になっていなければならない。
        つまり、常ならずグラフのありうる点の最大数とは、レーティング変動の谷と山の合計数に、始点と終点の2点を加えた数の事である。
        なお,レーティング変動に谷と山がなければ、常ならずグラフは作成できない。

    計算量；O(N)
    """

    n = int(input())
    A = list(map(int, input().split()))

    # コンテスト参加回数が1回の時は、グラフを作成することは出来ない
    if n == 1:
        print(0)
        exit()

    # 最初の2点の見た時、1番目より2番目が高ければ上昇フラグをたて、その逆であれば減少フラグをたてる。
    if A[0] < A[1]:
        flg = "UP"
    elif A[0] > A[1]:
        flg = "DOWN"
    else:
        # もし1番目と2番目のレーティングが等しければ、等しいレーティングを抜けるまでi-1とiを比較し続ける
        for i in range(1, n):
            if A[i - 1] != A[i]:
                flg = "UP" if A[i - 1] < A[i] else "DOWN"
                break
        # もし全てのレーティングが等しければ、常ならずグラフは作成できない
        else:
            print(0)
            exit()

    # 谷と山の合計数を調べる
    cnt = 0
    for i in range(1, n):
        # 谷の数をカウント
        if A[i - 1] < A[i] and flg == "DOWN":
            cnt += 1
            flg = "UP"
        # 山の数をカウント
        elif A[i - 1] > A[i] and flg == "UP":
            cnt += 1
            flg = "DOWN"

    print(0 if cnt == 0 else cnt + 2)


if __name__ == '__main__':
    resolve()
