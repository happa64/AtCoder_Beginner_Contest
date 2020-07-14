# https://atcoder.jp/contests/aising2020/submissions/15236779
# D - Anything Goes to Zero
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    X = input()
    cnt_init = X.count("1")
    x = int(X, 2)
    a = x % (cnt_init + 1)
    if cnt_init - 1 != 0:
        b = x % (cnt_init - 1)

    for i in range(n):
        if X[i] == "0":
            cnt = cnt_init + 1
            y = (a + pow(2, n - i - 1, cnt)) % cnt
        else:
            cnt = cnt_init - 1
            if cnt == 0:
                print(0)
                continue
            y = (b - pow(2, n - i - 1, cnt)) % cnt

        res = 1
        while y:
            cnt = bin(y).count("1")
            y %= cnt
            res += 1
        print(res)


if __name__ == '__main__':
    resolve()
