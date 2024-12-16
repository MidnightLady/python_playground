import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.minHeap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heapreplace(self.minHeap, val)

        print(val, self.minHeap)
        return self.minHeap[0]


l = KthLargest(5, [4, 5, 8, 2])  # l = [2, 4, 5, 8]
l.add(7)
l.add(7)
l.add(7)
l.add(2)
l.add(6)

import heapq


class MedianFinder:
    def __init__(self):
        # Max heap for the left half
        self.left = []
        # Min heap for the right half
        self.right = []

    def add_num(self, num):
        # Add to max heap (negative values for max heap behavior)
        heapq.heappush(self.left, -num)

        # Balance: Move the largest of the left heap to the right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Ensure left heap always has equal or more elements
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def find_median(self):
        # If odd, return the middle element
        if len(self.left) > len(self.right):
            return -self.left[0]
        # If even, return the average of two middle elements
        return (-self.left[0] + self.right[0]) / 2


# Example usage:
median_finder = MedianFinder()
data = [1, 3, 4, 2, 5]
for num in data:
    median_finder.add_num(num)
    print(f"Added {num}, Median: {median_finder.find_median()}")

median_finder.add_num(6)

print(median_finder.left)
print(median_finder.right)

median_finder.add_num(9)
print(median_finder.left)
print(median_finder.right)
