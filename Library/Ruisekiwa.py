# 二次元累積和
R = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        R[i + 1][j + 1] = R[i][j + 1] + R[i + 1][j] - R[i][j] + D[i][j]

res = [0 for _ in range(n * n + 1)]
for x1 in range(n):
    for x2 in range(x1 + 1, n + 1):
        for y1 in range(n):
            for y2 in range(y1 + 1, n + 1):
                area = (x2 - x1) * (y2 - y1)
                sum = R[x2][y2] - R[x1][y2] - R[x2][y1] + R[x1][y1]
                res[area] = max(res[area], sum)

for i in range(n * n):
    res[i + 1] = max(res[i + 1], res[i])
