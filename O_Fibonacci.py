def fibo(n,dp):
    if n==1:
        return 0
    if n==2:
        return 1
    if dp[n]!=-1:
        return dp[n]
    dp[n] = fibo(n-1,dp)+fibo(n-2,dp)
    return dp[n]


n = int(input())
dp = [-1]*(n+1)
fibonacci = fibo(n,dp)
print(fibonacci)