n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    w = int(input("Enter weight: "))
    v = int(input("Enter value: "))
    weights.append(w)
    values.append(v)

capacity = int(input("Enter knapsack capacity: "))

# Create DP table
dp = [[0] * (capacity + 1) for i in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):

        if weights[i - 1] <= w:
            include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
            exclude = dp[i - 1][w]
            dp[i][w] = max(include, exclude)

        else:
            dp[i][w] = dp[i - 1][w]

print("Maximum value:", dp[n][capacity])
