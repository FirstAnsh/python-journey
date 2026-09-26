raw_input = input("Enter heights separated by spaces: ")
heights = [int(x) for x in raw_input.split()]

left = 0
right = len(heights) - 1
max_area = 0

while left < right:
    # Width is the distance between the two pointers
    width = right - left
    # Water height is limited by the shorter line
    current_height = min(heights[left], heights[right])
    current_area = width * current_height
    
    max_area = max(max_area, current_area)

    # Move the pointer pointing to the shorter vertical line inward
    if heights[left] < heights[right]:
        left += 1
    else:
        right -= 1

print(f"Maximum water that can be contained: {max_area}")