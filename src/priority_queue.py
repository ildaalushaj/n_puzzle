import heapq


def to_tuple(grid):
    return tuple([tuple(row) for row in grid])


class PriorityQueue:
    entry_count = 0

    def __init__(self):
        self.elements = []
        self.dic_node = {}

    def empty(self):
        return len(self.elements) == 0

    def put(self, priority, item):
        PriorityQueue.entry_count += 1
        heapq.heappush(self.elements, (priority, PriorityQueue.entry_count, item))
        self.dic_node[to_tuple(item.grid)] = item

    def get(self):
        node = heapq.heappop(self.elements)
        del self.dic_node[to_tuple(node[2].grid)]
        return node[2]

    def is_in_heap(self, target):
        grid = to_tuple(target.grid)
        if grid in self.dic_node:
            return self.dic_node[grid], True
        return False, False
