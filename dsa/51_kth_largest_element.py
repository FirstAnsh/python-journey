import heapq

raw_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in raw_input.split()]
k = int(input("Enter k: "))

if k > len(nums) or k <= 0:
    print("Invalid value for k.")
else:
    # Create a min-heap to store the top k elements
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        # If the heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    # The root of the min-heap is the kth largest element
    kth_largest = min_heap[0]
    print(f"The {k}th largest element is: {kth_largest}")