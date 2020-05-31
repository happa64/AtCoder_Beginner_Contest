# https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b
# B - Qualification simulator
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    S = input()

    cnt = 0
    cnt_b = 0
    for s in S:
        if cnt < a + b:
            if s == "a":
                print("Yes")
                cnt += 1
            elif s == "b":
                if cnt_b < b:
                    print("Yes")
                    cnt += 1
                    cnt_b += 1
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")


if __name__ == '__main__':
    resolve()
