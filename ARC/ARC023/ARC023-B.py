# https://atcoder.jp/contests/arc023/submissions/13468942
# B - 謎の人物X
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        i + j <= Dであることは自明である。
        また、Dの偶奇によって、到達できるマスは制限される。具体的には(i + j)とDの偶奇が一致しているマスにのみ到達できる。
        よってマスを全探索し、上記の2条件にあてはまるマスの中で、最も値段が高いものが解となる。

    計算量：O(RC)
    """
    R, C, D = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(R)]

    res = []
    for i in range(R):
        for j in range(C):
            if (i + j) % 2 == D % 2 and i + j <= D:
                res.append(A[i][j])

    print(max(res))


if __name__ == '__main__':
    resolve()
