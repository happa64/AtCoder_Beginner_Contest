# https://atcoder.jp/contests/agc020/submissions/15375156
# B - Ice Rink Game
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k = int(input())
    A = list(map(int, input().split()))[::-1]

    if A[0] != 2:
        print(-1)
    else:
        prev_min, prev_max = 2, 3
        for i in range(1, k):
            a = A[i]
            if a > prev_max:
                print(-1)
                break
            else:
                if prev_min % a == 0:
                    now_min = prev_min
                else:
                    now_min = (prev_min // a + 1) * a
                if now_min > prev_max:
                    print(-1)
                    break
                diff = prev_max - now_min
                now_max = now_min + (diff // a + 1) * a - 1
                prev_min, prev_max = now_min, now_max
        else:
            print(prev_min, prev_max)


if __name__ == '__main__':
    resolve()
