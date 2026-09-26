raw_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in raw_input.split()]

if not nums:
    print("Length of LIS: 0")
else:
    # dp[i] stores the length of the longest increasing subsequence ending at index i
    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_lis = max(dp)
    print(f"Length of Longest Increasing Subsequence: {max_lis}")