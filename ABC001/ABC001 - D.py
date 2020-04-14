import sys

sys.setrecursionlimit(10 ** 7)


def resolve():
    n = int(input())
    memo = []
    for i in range(n):
        se = list(input())
        if 1 <= int(se[3]) <= 4:
            se[3] = "0"
        elif 6 <= int(se[3]) <= 9:
            se[3] = "5"

        if 1 <= int(se[8]) <= 4:
            se[8] = "5"
        elif 6 <= int(se[8]) <= 9:
            se[8] = "0"
            if se[7] != "5":
                se[7] = str(int(se[7]) + 1)
            else:
                se[7] = "0"
                if se[6] != "9":
                    se[6] = str(int(se[6]) + 1)
                else:
                    se[6] = "0"
                    se[5] = str(int(se[5]) + 1)
        start = "".join(se[0: 4])
        end = "".join(se[5: 9])
        memo.append([int(start), int(end)])

    memo = sorted(memo, key=lambda x: x[0])
    t = [memo[0]]
    for i in range(1, n):
        start, end = t[-1]
        next_start, next_end = memo[i]
        if end < next_start:
            t.append(memo[i])
        else:
            t[-1][1] = max(end, next_end)

    for start, end in t:
        res = (str(start).zfill(4) + "-" + str(end).zfill(4))
        print(res)


if __name__ == '__main__':
    resolve()
