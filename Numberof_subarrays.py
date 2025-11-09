# Problem Statement
# Given an integer N representing the number of elements in an array, find the total number of subarrays that can be generated from it.
# Formula
# Total Subarrays=N×(N+1)2\text{Total Subarrays} = \frac{N \times (N + 1)}{2}Total Subarrays=2N×(N+1)
# Input Format
# ● An integer N, the size of the array.
# Output Format
# ● Print the total number of subarrays possible.
# Example
# Input:
# N = 4
# Output:
# 10
# Explanation
# For an array of size 4 → [a, b, c, d],
# Total subarrays = 4 × (4 + 1) / 2 = 10.

N=int(input("Enter the size of the array (N): "))
total_subarrays=N*(N+1)//2 
print("Total number of subarrays:",total_subarrays)