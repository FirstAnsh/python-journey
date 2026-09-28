import heapq
from collections import Counter

raw_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in raw_input.split()]
k = int(input("Enter k: "))

# Step 1: Count the frequency of each number
frequency_map = Counter(nums)

# Step 2: Use a min-heap to keep track of the top k elements.
# The heap will store tuples of (frequency, number).
min_heap = []

for num, freq in frequency_map.items():
    heapq.heappush(min_heap, (freq, num))
    # If heap size exceeds k, evict the element with the lowest frequency
    if len(min_heap) > k:
        heapq.heappop(min_heap)

# Step 3: Extract the elements from the heap (order doesn't matter for the final output)
top_k_elements = [num for freq, num in min_heap]

print(f"The top {k} frequent elements are: {top_k_elements}")