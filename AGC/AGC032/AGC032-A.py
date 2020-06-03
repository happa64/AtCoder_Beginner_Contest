# https://atcoder.jp/contests/agc032/tasks/agc032_a
# A - Limited Insertion
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    B = list(map(int, input().split()))

    res = []
    # Bを調べた時、j=B[j]かつ一番右側にあるものが、直前に挿入した整数である
    for i in range(n):
        L = len(B)
        # 上記条件に合うものを、後ろから見ていき、配列に順に入れていく
        for j in reversed(range(L)):
            if j + 1 == B[j]:
                res.append(B[j])
                B.pop(j)
                break
        # 条件にあうものが無ければ、達成不可能
        else:
            print(-1)
            exit()

    res = res[::-1]
    for i in res:
        print(i)


if __name__ == '__main__':
    resolve()
