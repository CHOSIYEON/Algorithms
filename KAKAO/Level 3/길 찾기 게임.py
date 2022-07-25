import sys
sys.setrecursionlimit(10 ** 6)

def preorder(nodes, answer):
    node = nodes[0]
    left, right = [], []

    for i in range(1, len(nodes)):
        if node[0] > nodes[i][0]:
            left.append(nodes[i])
        else:
            right.append(nodes[i])

    answer.append(node[2])

    if left:
        preorder(left, answer)

    if right:
        preorder(right, answer)

    return


def postorder(nodes, answer):
    node = nodes[0]
    left, right = [], []

    for i in range(1, len(nodes)):
        if node[0] > nodes[i][0]:
            left.append(nodes[i])
        else:
            right.append(nodes[i])

    if left:
        postorder(left, answer)

    if right:
        postorder(right, answer)

    answer.append(node[2])
    
    return


def solution(nodeinfo):
    pre, post = [], []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))

    preorder(nodeinfo, pre)
    postorder(nodeinfo, post)

    return [pre, post]