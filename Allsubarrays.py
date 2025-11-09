# Problem Statement
# Given an array of integers, print all possible subarrays and their elements.
# Input Format
# ● First line: integer N (size of array)
# ● Second line: N integers (array elements)
# Output Format
# ● Print all subarrays, one per line.

N=int(input())
arr=list(map(int,input().split()))
for start in range(N):
    for end in range(start, N):
        for i in range(start,end+1):
            print(arr[i],end=' ')
        print()