#2250 아 진짜,,,.,.,., 나는 바보다 루트노드찾는거를 이상하게 짜서 이상하게 꼬인거를 왜 발견을 이렇게 늦게한걸까,,,,,,,,,
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[-1, -1, -1] for _ in range(n + 1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a][1] = b
    tree[a][2] = c
    if c > 0 :
        tree[c][0] = -2
    if b > 0 :
        tree[b][0] = -2
root = a
for _ in range(1, n + 1):
    if tree[_][0] == -1:
        root = _
visited = [[0, 0] for _ in range(n + 1)]
lev_w = [[-1, -1] for _ in range(n + 1)]
q = deque([root])
visited[root][0] = 1
lev_w[root][0] = 1

while q:
    tmp = q.popleft()
    for i in tree[tmp][1:]:
        if not visited[i][0] and i != -1:
            visited[i][0] = 1
            q.append(i)
            lev_w[i][0] = lev_w[tmp][0] + 1
w = 1


def pre(node, lev_w):
    global w
    if node != -1:
        pre(tree[node][1], lev_w)
        lev_w[node][1] = w
        w += 1
        pre(tree[node][2], lev_w)


pre(root, lev_w)
lev_w.sort(key=lambda x: x[0])
tmp = [[] for _ in range(n + 1)]
for level, wide in lev_w:
    if level == wide == -1:
        continue
    tmp[level].append(wide)
ans_lev, ans_wid = 0, 0
for i, t in enumerate(tmp):
    if not t:
        continue
    right, left = max(t), min(t)
    if ans_wid < right - left + 1:
        ans_wid = right - left + 1
        ans_lev = i
print('{} {}'.format(ans_lev, ans_wid))
