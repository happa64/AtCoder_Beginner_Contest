def topological_sort(edge):
    from collections import deque
    n = len(edge)
    res = []
    ind = [0] * n
    for v in range(n):
        for u in edge[v]:
            ind[u] += 1
    que = deque([i for i in range(n) if ind[i] == 0])
    while que:
        v = que.popleft()
        res.append(v + 1)
        for u in edge[v]:
            ind[u] -= 1
            if ind[u] == 0:
                que.append(u)
    return res if len(res) == n else False
