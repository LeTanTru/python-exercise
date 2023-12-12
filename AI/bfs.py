from collections import defaultdict
import time


class Node:
    def __init__(self, name, par=None):
        self.name = name
        self.par = par


data = defaultdict(list)
data["A"] = ["B", "C", "D"]
data["B"] = ["C", "E", "F"]
data["C"] = ["F", "G", "H"]
data["D"] = ["I", "J"]
data["F"] = ["K", "L", "M"]
data["H"] = ["N", "O"]


def is_equal(src, dest):
    return src.name == dest.name if src is not None and dest is not None else False


def print_path(v):
    result = []
    while v:
        result.append(v.name)
        v = v.par

    result.reverse()
    print(" -> ".join(result))


def is_contain(v, queue) -> bool:
    for x in queue:
        if is_equal(x, v):
            return True
    return False


def bfs(_src, _dest):
    src = Node(_src)
    dest = Node(_dest)
    queue = []
    visited = []
    queue.append(src)
    i = 1
    is_found_path = False
    while queue:
        v = queue.pop(0)
        visited.append(v)
        if is_equal(v, dest):
            print(f"Path {i}: ", end="")
            i += 1
            print_path(v)
            is_found_path = True

        for x in data[v.name]:
            temp = Node(x)
            temp.par = v
            queue.append(temp)
    return is_found_path


start_time = time.time()

is_found_path = bfs("A", "I")
if not is_found_path:
    print("Not found !")

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Run in: {elapsed_time}s")
