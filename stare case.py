def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    
    # Initialize a list to store the number of ways to reach each step
    dp = [0] * (n + 1)
    
    # There's only one way to reach the 0th step
    dp[0] = 1
    # There's only one way to reach the 1st step
    dp[1] = 1
    
    # Iterate from step 2 to n
    for i in range(2, n + 1):
        # The number of ways to reach the current step is the sum of
        # the number of ways to reach the previous two steps
        dp[i] = dp[i - 1] + dp[i - 2]
    
    # The final answer is the number of ways to reach the nth step
    return dp[n]

# Take input from the user
n = int(input("Enter the number of steps: "))
print("Number of distinct ways to climb the staircase with", n, "steps:", climbStairs(n))
