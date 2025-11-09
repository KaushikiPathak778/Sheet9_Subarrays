# Problem Statement
# Given an integer array and two indices L and R, find the sum of elements between those indices (inclusive).
# Input Format
# ● First line: integer N
# ● Second line: N space-separated integers
# ● Third line: two integers L and R (1-based index)
# Output Format
# ● Print the sum of elements from index L to R.
# Example
# Input:
# 5
# 1 2 3 4 5
# 2 4
# Output:
# 9
# Explanation
# Subarray from index 2 to 4 → [2, 3, 4]
# Sum = 2 + 3 + 4 = 9

N=int(input())
arr=list(map(int,input().split()))
L,R=map(int,input().split())
L-=1
R-=1
print(sum(arr[L:R+1]))