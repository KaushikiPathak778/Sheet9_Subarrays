# Problem Statement
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Input Format
# ● First line: integer N
# ● Second line: N integers (array elements)
# Output Format
# ● Print the maximum subarray sum.
# Example
# Input:
# 8
# -2 1 -3 4 -1 2 1 -5 4
# Output:
# 6
# Explanation
# The subarray [4, -1, 2, 1] has the largest sum = 6.

N=int(input())
nums=list(map(int,input().split()))
max_sum=current_sum=nums[0]
for i in range(1,N):
    current_sum=max(nums[i],current_sum+nums[i])
    max_sum=max(max_sum,current_sum)
print(max_sum)