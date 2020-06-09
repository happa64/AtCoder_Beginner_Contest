import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input()) + 1
    player = ["Aoki", "Takahashi"]

    win = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (n // 2 + 1) if win else n // 2
        win ^= 1

    print(player[win])


if __name__ == '__main__':
    resolve()
