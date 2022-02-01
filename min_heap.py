class MinHeap:
    heap_array = []

    def min_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        heap_length = len(self.heap_array) - 1

        if left < heap_length and self.heap_array[left] < self.heap_array[smallest]:
            smallest = left
        if right < heap_length and self.heap_array[right] < self.heap_array[smallest]:
            smallest = right

        if smallest != i:
            self.heap_array[i], self.heap_array[smallest] = self.heap_array[smallest], self.heap_array[i]
            self.min_heapify(smallest)

    def insert_key(self, key):
        self.heap_array.append(key)
        i = len(self.heap_array) - 1
        while i != 0 and self.heap_array[i] < self.heap_array[self.parent(i)]:
            self.heap_array[i], self.heap_array[self.parent(i)] = self.heap_array[self.parent(i)], self.heap_array[i]
            i = self.parent(i)

    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.extract_min()

    def increase_key(self, i, val):
        self.heap_array[i] = val
        self.min_heapify(i)

    def decrease_key(self, i, val):
        self.heap_array[i] = val

        while i != 0 and self.heap_array[i] < self.heap_array[self.parent(i)]:
            self.heap_array[i], self.heap_array[self.parent(i)] = self.heap_array[self.parent(i)], self.heap_array[i]
            i = self.parent(i)

    def get_min(self):
        return self.heap_array[0]

    def extract_min(self):
        if len(self.heap_array) == 1:
            min = self.heap_array[0]
            del self.heap_array[0]
            return min
        min = self.heap_array[0]

        self.heap_array[0] = self.heap_array[len(self.heap_array) - 1]
        del self.heap_array[len(self.heap_array) - 1]

        self.min_heapify(0)

        return min

    def parent(self, i):
        return (i - 1) // 2


heap = MinHeap()
heap.insert_key(3)
heap.insert_key(2)
heap.delete_key(1)
heap.insert_key(15)
heap.insert_key(5)
heap.insert_key(4)
heap.insert_key(45)

print(heap.extract_min(), end=" ")
print(heap.get_min(), end=" ")

heap.decrease_key(2, 1)

print(heap.get_min())