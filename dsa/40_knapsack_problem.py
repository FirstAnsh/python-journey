capacity = int(input("Enter maximum knapsack capacity: "))
weights = [int(w) for w in input("Enter item weights (space-separated): ").split()]
values = [int(v) for v in input("Enter item values (space-separated): ").split()]

n = len(weights)

# dp[i][w] will store the max value attainable using a subset of the first i items
# with an available weight limit w
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacity + 1):
        current_weight = weights[i - 1]
        current_val = values[i - 1]

        if current_weight <= w:
            # Choose max of:
            # 1. Take the current item: current_val + dp[i - 1][w - current_weight]
            # 2. Leave the current item: dp[i - 1][w]
            dp[i][w] = max(dp[i - 1][w], current_val + dp[i - 1][w - current_weight])
        else:
            # Cannot include current item as it exceeds current capacity limit w
            dp[i][w] = dp[i - 1][w]

print(f"Maximum achievable value: {dp[n][capacity]}")