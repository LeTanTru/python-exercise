from collections import defaultdict
import time


class Node:
    def __init__(self, name, par=None):
        self.name = name
        self.par = par
        self.depth = 0


data = defaultdict(list)
data["A"] = ["B", "C", "D"]
data["B"] = ["C", "E", "F"]
data["C"] = ["F", "G", "H"]
data["D"] = ["I", "J"]
data["F"] = ["K", "L", "M"]
data["H"] = ["N", "O"]


def is_equal(src, dest):
    return src.name == dest.name if src is not None and dest is not None else False


def path(v):
    result = []
    while v:
        result.append(v.name)
        v = v.par
    result.reverse()
    print(" -> ".join(result))


def init_depth():
    new_data = []
    print(len(data))
    for node in data:
        new_node = Node(node)
        new_data.append(new_node)
        for x in data[node]:
            temp = Node(x)
            temp.par = node
            temp.depth = 0
            new_data.append(temp)
    for node in new_data:
        node.depth = Node(node.par).depth + 1
    return new_data


def dfs(_src, _dest) -> bool:
    src = Node(_src)
    dest = Node(_dest)

    stack = []
    result = []
    stack.append(src)
    i = 1
    is_found_path = False
    while stack:
        v = stack.pop(0)

        if is_equal(v, dest):
            print(f"Path {i}: ", end="")
            i += 1
            path(v)
            is_found_path = True

        pos = 0
        for x in data[v.name]:
            temp = Node(x)
            temp.par = v

            stack.insert(pos, temp)
            pos += 1
    return is_found_path


new_data = init_depth()

# for node in new_data:
#     print([node.name, node.par, node.depth])

# start_time = time.time()

# is_found_path = dfs("A", "M")
# if not is_found_path:
#     print("Not found !")

# end_time = time.time()

# elapsed_time = end_time - start_time

# print(f"Run in: {elapsed_time}s")
