# https://atcoder.jp/contests/abc059/submissions/13127654
# C - Sequence
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    cnt_odd_plus, cnt_odd_minus = 0, 0
    R_plus, R_minus = [0], [0]
    for i in range(n):
        if i % 2 == 0:
            # 奇数番目までの和をプラスにしたいのに、0以下になってしまう場合は和が1になるように操作する
            if R_plus[-1] + A[i] <= 0:
                cnt_odd_plus += 1 - (R_plus[-1] + A[i])
                R_plus.append(1)
            else:
                R_plus.append(R_plus[-1] + A[i])

            # 奇数番目までの和をマイナスにしたいのに、0以上になってしまう場合は和が1になるように操作する
            if R_minus[-1] + A[i] >= 0:
                cnt_odd_minus += 1 + (R_minus[-1] + A[i])
                R_minus.append(-1)
            else:
                R_minus.append(R_minus[-1] + A[i])
        else:
            # 偶数番目までの和をマイナスにしたいのに、0以上になってしまう場合は和が-1になるように操作する
            if R_plus[-1] + A[i] >= 0:
                cnt_odd_plus += 1 + (R_plus[-1] + A[i])
                R_plus.append(-1)
            else:
                R_plus.append(R_plus[-1] + A[i])

            # 偶数番目までの和をプラスにしたいのに、0以下になってしまう場合は和が1になるように操作する
            if R_minus[-1] + A[i] <= 0:
                cnt_odd_minus += 1 - (R_minus[-1] + A[i])
                R_minus.append(1)
            else:
                R_minus.append(R_minus[-1] + A[i])

    res = min(cnt_odd_plus, cnt_odd_minus)
    print(res)


if __name__ == '__main__':
    resolve()
