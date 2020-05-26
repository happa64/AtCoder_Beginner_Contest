# https://atcoder.jp/contests/tenka1-2017/submissions/12890787
# C - 4/N
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N = int(input())

    # hとnを決め打ちし、wを計算で求める
    for h in range(1, 3501):
        for n in range(1, 3501):
            if 4 * h * n - N * n - N * h > 0:
                w = (N * h * n) / (4 * h * n - N * n - N * h)

                # wが正整数かつ、問題文の式を変形し、除算を取り除いた式に当てはまればok
                if w.is_integer() and w > 0 and 4 * h * n * w == N * n * w + N * h * w + N * h * n:
                    print(h, n, int(w))
                    exit()


if __name__ == '__main__':
    resolve()
