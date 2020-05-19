# https://atcoder.jp/contests/abc065/submissions/13398961
# A - Expired?
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, a, b = map(int, input().split())
    late = a - b
    # 賞味期限が過ぎていなければ、美味しい
    if late >= 0:
        print("delicious")
    else:
        # 賞味期限が過ぎていても、それがx日以内であれば問題なし
        if x + late >= 0:
            print("safe")
        # x日を超えていれば、お腹を壊す
        else:
            print("dangerous")


if __name__ == '__main__':
    resolve()
