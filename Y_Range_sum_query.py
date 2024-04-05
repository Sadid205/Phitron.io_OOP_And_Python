N,Q = input().split()
N = int(N)
Q = int(Q)
A = list(map(int,input().split()))
N = len(A)
pre = [None]*N
pre[0] = A[0]
for i in range(1,N):
    pre[i] = A[i]+pre[i-1]
for i in range(Q):
    L,R = input().split()
    L = int(L)-1
    R = int(R) -1
    sum
    if L==0:
        sum = pre[R]
    else:
        sum = pre[R] - pre[L-1]
    
    print(sum)



