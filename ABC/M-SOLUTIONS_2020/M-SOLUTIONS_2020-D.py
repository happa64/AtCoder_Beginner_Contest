import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    kai = set()
    uri = set()
    i = 1
    while i < n:
        if A[i - 1] < A[i]:
            kai.add(i - 1)
            while i < n and A[i - 1] <= A[i]:
                i += 1
            uri.add(i - 1)
            while i < n and A[i - 1] >= A[i]:
                i += 1
        else:
            i += 1

    if len(kai) == 0:
        print(1000)
        exit()

    money = 1000
    kabu = 0
    for i in range(n):
        if i in kai:
            if i == n - 1:
                continue
            kabu, money = divmod(money, A[i])
        elif i in uri:
            money += kabu * A[i]
            kabu = 0
    print(money)


if __name__ == '__main__':
    resolve()
