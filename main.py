from collections import Counter


class Heap:
    def __init__(self):
        self.store = [0]
        self.count = 0

    def push(self, item):
        """
        :param item: element to be pushed in the heap
        :return: None

        Algorithm:
        1. Insert the element at the end of the list
        2. Move the element to the appropriate place
        """
        self.count += 1
        index = self.count
        self.store.append(item)

        while index > 1:
            parent = index // 2
            if self.store[parent][1] < self.store[index][1]:
                self.store[parent], self.store[index] = self.store[index], self.store[parent]
                index = parent
            else:
                return

    def pop(self):
        """
        :return: return the top element

        Algorithm:
        1. replace the root element with the last element
        2. move the last element to the approriate place
        """
        if self.count < 1:
            print("Heap is empty")
            return None
        if self.count == 1:
            self.count -= 1
            return self.store.pop()

        item = self.store[1]
        self.store[1] = self.store.pop()
        self.count -= 1
        index = 1

        while index < self.count:
            left_child = 2 * index
            right_child = 2 * index + 1

            if left_child <= self.count and self.store[index][1] < self.store[left_child][1]:
                self.store[index], self.store[left_child] = self.store[left_child], self.store[index]
                index = left_child
            elif right_child <= self.count and self.store[index][1] < self.store[right_child][1]:
                self.store[index], self.store[right_child] = self.store[right_child], self.store[index]
                index = right_child
            else:
                return item
        return item

    def print(self):
        print(self.store)


def topKFrequent(nums, k):
    if len(nums) == k:
        return nums

    frequency = Counter(nums)
    heap = Heap()

    for item in frequency.items():
        heap.push(item)
    item = []
    for i in range(k):
        item.append(heap.pop()[0])

    return  item

ans = topKFrequent([1, 1, 1, 2, 2, 3], 2)
ans = topKFrequent([1,1,1], 1)
print(ans)
