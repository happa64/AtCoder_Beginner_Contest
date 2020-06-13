# https://atcoder.jp/contests/abc046/submissions/14211289
# C - AtCoDeerくんと選挙速報
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    TA = [list(map(int, input().split())) for _ in range(n)]

    t_pev, a_prev = TA[0]
    for i in range(1, n):
        t_now, a_now = TA[i]
        if t_pev <= t_now and a_prev <= a_now:
            t_pev, a_prev = t_now, a_now
        else:
            d = max((t_pev + (t_now - 1)) // t_now, (a_prev + (a_now - 1)) // a_now)
            t_pev, a_prev = t_now * d, a_now * d
    print(t_pev + a_prev)


if __name__ == '__main__':
    resolve()
