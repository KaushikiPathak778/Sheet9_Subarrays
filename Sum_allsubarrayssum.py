# Problem Statement
# Given an integer array, find the sum of all subarray sums using the Contribution Technique.
# Concept
# Each element at index i contributes to several subarrays:
# Contribution of element i=arr[i]×(i+1)×(N−i)\text{Contribution of element i} = \text{arr[i]} \times (i + 1) \times (N - i)Contribution of element i=arr[i]×(i+1)×(N−i)
# Input Format
# ● First line: integer N
# ● Second line: N integers (array elements)
# Output Format
# ● Print the total sum of all subarray sums.

N=int(input())
arr=list(map(int,input().split()))
total_sum=0
for i in range(N):
    contribution=arr[i]*(i+1)*(N-i)
    total_sum+=contribution
print(total_sum)