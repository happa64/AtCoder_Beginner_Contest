# https://atcoder.jp/contests/abc175/submissions/15940976
# D - Moving Piece
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    res = -f_inf
    for now in range(n):
        cnt = 0
        score = [0]
        visited = set()
        for j in range(k):
            next_now = P[now] - 1
            if next_now not in visited:
                score.append(score[-1] + C[next_now])
                visited.add(next_now)
                now = next_now
                cnt += 1
            else:
                break
        score.pop(0)
        if k - cnt == 0:
            res = max(res, max(score))
        else:
            if score[-1] <= 0:
                res = max(res, max(score))
            else:
                q, r = divmod(k, cnt)
                if r == 0:
                    res = max(res, max(score) + score[-1] * (q - 1))
                else:
                    res = max(res, max(score[:r]) + score[-1] * q, max(score[r:]) + score[-1] * (q - 1))
    print(res)


if __name__ == '__main__':
    resolve()
