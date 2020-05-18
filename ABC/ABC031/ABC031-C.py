# https://atcoder.jp/contests/abc031/submissions/13377132
# C - 数列ゲーム
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要；
        高橋君の〇の位置を決めた時、青木君のスコアが最大値になる時が、高橋君のスコアとなる。
        これは高橋君の〇の位置を固定し、青木君の〇の位置を全探索することによって求める。
        よって、高橋君の〇の位置を全探索し、更に青木君の〇の位置を全探索することで解が求まる。

    計算量；O(N^3)
    """

    n = int(input())
    A = list(map(int, input().split()))

    # ans：最終的な解。負の値をとる場合がある為、負の無限大で初期化する
    ans = -f_inf

    # t：高橋君の〇の位置、a：青木君の〇の位置
    for t in range(n):
        # score_t_list:tを決め打ちし、aを全探索した時の高橋君の各スコア
        # score_a_list:tを決め打ちし、aを全探索した時の青木君の各スコア
        score_a_list, score_t_list = [], []
        for a in range(n):
            if t == a:
                continue
            right, left = min(t, a), max(t, a)

            # sub：tとaを決め打ちした時の数列
            sub = A[right: left + 1]
            # score_a：subsにおける青木君のスコア、score_t：subsにおける高橋君のスコア
            score_a, score_t = 0, 0
            for i in range(len(sub)):
                if i % 2:
                    score_a += sub[i]
                else:
                    score_t += sub[i]

            score_a_list.append(score_a)
            score_t_list.append(score_t)

        # max_score_a:tを決め打ちした時の、青木君の最大スコア。負の値をとる場合がある為、負の無限大で初期化する
        max_score_a = -f_inf

        res = 0
        # 青木君の各スコアを"左から"見ていき、最大値をとるインデックスが、高橋君のスコアのインデックスとなる
        for idx, score in enumerate(score_a_list):
            if max_score_a < score:
                max_score_a = score
                res = idx

        # 高橋君のスコアの最大値を更新していく
        ans = max(ans, score_t_list[res])

    print(ans)


if __name__ == '__main__':
    resolve()
