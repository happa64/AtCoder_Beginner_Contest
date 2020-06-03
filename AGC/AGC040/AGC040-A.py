# https://atcoder.jp/contests/agc040/tasks/agc040_a
# A - ><
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)

    # 先頭から>の数を数えていき、<になったらゼロにする
    A = [0] * (n + 1)
    cnt = 0
    for i in range(n):
        if s[i] == "<":
            cnt += 1
            A[i + 1] = cnt
        else:
            cnt = 0

    # 末尾から<の数を数えていき、>になったらゼロにする
    B = [0] * (n + 1)
    cnt = 0
    for i in reversed(range(n)):
        if s[i] == ">":
            cnt += 1
            B[i] = cnt
        else:
            cnt = 0

    # 上記二つの比較した時の大きい方の値の和が答えとなる
    res = 0
    for i in range(n + 1):
        res += max(A[i], B[i])

    print(res)


if __name__ == '__main__':
    resolve()
