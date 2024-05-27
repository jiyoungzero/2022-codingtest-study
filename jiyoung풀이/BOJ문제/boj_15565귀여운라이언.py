import sys
input = sys.stdin.readline 


n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = int(1e9)

# 1이 k개 이상 포함된, 연속된 가장 작은 길이
s, e = 0, 0
cnt = 1 if arr[s] == 1 else 0
while e < n:
    e += 1
    if cnt >= k:
        if answer > e-s+1:
            answer = e-s+1
            s += 1
    
    if arr[e] == 1:
        cnt += 1
    
print(answer if answer < int(1e9) else -1)