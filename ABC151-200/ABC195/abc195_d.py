 


    # dp = [[0]*(len(box)) for _ in range(N+1)]

    # for i in range(len(box)):
    #     for j in range(N):
    #         if box[i] < WV[j]:
    #             pass
    #         else:
    #             dp[i+1][j] = max(dp[i][j], dp[i])

    # dp = [[0]*(len(box)) for j in range(N+1)]

    # for i in range(N):
    #     for j in range(len(box)):
    #         if WV[i] > box[j]: # 荷物の重さ > 箱の容量
    #             dp[i+1][j] = dp[i][j]
    #         else: # 選ぶ時
    #             dp[i+1][j] = max(dp[i][j],dp[i][j-box[i]]+WV[i])