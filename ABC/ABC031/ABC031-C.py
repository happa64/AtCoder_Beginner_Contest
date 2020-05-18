# https://atcoder.jp/contests/abc031/submissions/13377132
# C - 数列ゲーム
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    ans = -f_inf
    # 高橋君の〇を決め打ちした時、青木君が最も高得点をとれる〇の位置を探す。
    for t in range(n):
        socre_a_list = []
        socre_t_list = []
        for a in range(n):
            if t == a:
                continue
            right, left = min(t, a), max(t, a)
            score_a, score_t = 0, 0
            sub = A[right: left + 1]
            for i in range(len(sub)):
                if i % 2:
                    score_a += sub[i]
                else:
                    score_t += sub[i]
            socre_a_list.append(score_a)
            socre_t_list.append(score_t)

        max_score_a = -f_inf
        res = 0
        for idx, score in enumerate(socre_a_list):
            if max_score_a < score:
                max_score_a = score
                res = idx

        ans = max(ans, socre_t_list[res])

    print(ans)


if __name__ == '__main__':
    resolve()
