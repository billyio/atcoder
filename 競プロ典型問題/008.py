# https://github.com/TeppeiSudo/kyopro_educational_90_python/blob/master/sol/008.py

# Step #1. Input
N = int(input())
S = str(input())
mod = 1000000007
dp = [[0]*8 for _ in range(N+1)]


# Step #2. Dynamic Programming (DP)
dp[0][0] = 1
for i in range(N):
    for j in range(8):
        dp[i+1][j] += dp[i][j]
        if (S[i] == "a") and (j == 0):
            dp[i+1][j+1] += dp[i][j]
        elif (S[i] == "t") and (j == 1):
            dp[i+1][j+1] += dp[i][j]
        elif (S[i] == "c") and (j == 2):
            dp[i+1][j+1] += dp[i][j]
        elif (S[i] == "o") and (j == 3):
            dp[i+1][j+1] += dp[i][j]
        elif (S[i] == "d") and (j == 4):
            dp[i+1][j+1] += dp[i][j]
        elif (S[i] == "e") and (j == 5):
            dp[i+1][j+1] += dp[i][j]
        elif (S[i] == "r") and (j == 6):
            dp[i+1][j+1] += dp[i][j]
            
    for j in range(8):
        dp[i+1][j] %= mod

# Step #3. Output the answer
print(dp[N][7])
