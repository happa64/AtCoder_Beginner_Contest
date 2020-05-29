# https://atcoder.jp/contests/past201912-open/tasks/past201912_d
# D - 重複検査
import sys
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    a = sorted(list(int(input()) for _ in range(n)))

    # 1~nが何個あるかカウント
    cnt = [0 for _ in range(n)]
    for i in range(n):
        if a[i] in range(1, n + 1):
            cnt[a[i] - 1] += 1

    # 書き換えた数値はカウントは2になっている
    # 書き換えられた数値はカウントが0になっている
    x, y = 0, 0
    for j in cnt:
        if j == 0:
            x = cnt.index(j) + 1
        elif j == 2:
            y = cnt.index(j) + 1

    if x != 0 and y != 0:
        print(y, x)
    else:
        print("Correct")


if __name__ == '__main__':
    resolve()
