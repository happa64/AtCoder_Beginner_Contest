# https://atcoder.jp/contests/arc017/submissions/13282717
# B - 解像度が低い。
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(int(input()) for _ in range(n))

    # 部分単調増加列の長さを配列Rに入れていく
    R = []
    cnt = 1
    for i in range(1, n):
        if A[i - 1] < A[i]:
            cnt += 1
        else:
            R.append(cnt)
            cnt = 1
    if cnt:
        R.append(cnt)

    # 部分単調増加列から、連続したk個の部分列の取り出し方は、部分単調増加列の長さ：i-k+1である
    res = 0
    for i in R:
        if i >= k:
            res += i - k + 1

    print(res)


if __name__ == '__main__':
    resolve()
