# https://atcoder.jp/contests/arc071/submissions/19486470
# E - TrBBnsformBBtion
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input().rstrip()
    t = input().rstrip()
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]

    cnt_s = [0] * (len(s) + 1)
    a = 0
    for i in range(len(s)):
        a += 1 if s[i] == "A" else 2
        cnt_s[i + 1] = a % 3

    cnt_t = [0] * (len(t) + 1)
    a = 0
    for i in range(len(t)):
        a += 1 if t[i] == "A" else 2
        cnt_t[i + 1] = a % 3

    for a, b, c, d in query:
        a_s = (cnt_s[b] - cnt_s[a - 1]) % 3
        a_t = (cnt_t[d] - cnt_t[c - 1]) % 3
        print("YES" if a_s == a_t else "NO")


if __name__ == '__main__':
    resolve()
