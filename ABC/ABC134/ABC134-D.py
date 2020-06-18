# https://atcoder.jp/contests/abc134/submissions/14453867
# D - Preparing Boxes
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    約数列挙解法。O(N√N)
    """
    n = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] * (n + 1)
    res = []

    for i in reversed(range(1, n + 1)):
        if B[i] % 2 != A[i]:
            res.append(i)
            for j in range(1, int(pow(i, 0.5)) + 1):
                if i % j == 0:
                    B[j] += 1
                    if j != i // j:
                        B[i // j] += 1

    print(len(res))
    if len(res) != 0:
        print(*res[::-1])


def resolve2():
    """
    想定解法。P(NlogN)
    """
    n = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] * (n + 1)

    for i in reversed(range(1, n + 1)):
        cnt = 0
        for j in range(i, n + 1, i):
            cnt += B[j]
        if cnt % 2 != A[i]:
            B[i] += 1

    print(sum(B))
    if sum(B) != 0:
        print(*[i for i, ball in enumerate(B) if ball])


if __name__ == '__main__':
    resolve2()
