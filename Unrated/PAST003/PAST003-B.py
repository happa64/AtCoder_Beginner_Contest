# https://atcoder.jp/contests/past202005-open/submissions/14079403
# B - ダイナミック・スコアリング
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N, M, Q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(Q)]

    scores = [[0 for _ in range(M)] for _ in range(N)]
    problems = [N for _ in range(M)]

    for i in range(Q):
        if query[i][0] == 1:
            _, n = query[i]
            total = 0
            for idx, flg in enumerate(scores[n - 1]):
                if flg == 1:
                    total += problems[idx]
            print(total)
        else:
            _, n, m = query[i]
            problems[m - 1] -= 1
            scores[n - 1][m - 1] = 1


if __name__ == '__main__':
    resolve()
