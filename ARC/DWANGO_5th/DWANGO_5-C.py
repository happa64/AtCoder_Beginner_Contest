# https://atcoder.jp/contests/dwacon5th-prelims/submissions/18682412
# C - k-DMC
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input().rstrip()
    _ = int(input())
    K = map(int, input().split())

    left_D = []
    cnt = 0
    for s in S:
        if s == "D":
            cnt += 1
        elif s == "M":
            left_D.append(cnt)

    for k in K:
        res = 0
        tot_cnt_D = 0
        cnt_M = 0
        cnt_D = 0
        left_pos = right_pos = 0
        for i in range(k):
            if S[i] == "M":
                tot_cnt_D += left_D[right_pos]
                right_pos += 1
                cnt_M += 1
            elif S[i] == "C":
                res += tot_cnt_D

        for right in range(k, n):
            left = right - k
            if S[left] == "M":
                tot_cnt_D -= left_D[left_pos]
                left_pos += 1
                cnt_M -= 1
            elif S[left] == "D":
                cnt_D += 1

            if S[right] == "M":
                tot_cnt_D += left_D[right_pos]
                right_pos += 1
                cnt_M += 1
            elif S[right] == "C":
                res += tot_cnt_D - cnt_D * cnt_M
        print(res)


if __name__ == '__main__':
    resolve()
