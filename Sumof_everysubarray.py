# Given an array of integers, print the sum of all possible subarrays.
# Input Format
# ● First line: integer N
# ● Second line: N integers (array elements)
# Output Format
# ● Print the sum of each subarray, one per line.


N=int(input())
arr=list(map(int,input().split()))
for start in range(N):
    total=0
    for end in range(start,N):
        total+=arr[end]
        print(total)