# Find all subsets/Power set

def print_subset(subset):
    print("{", end="")
    for i in subset:
        if i is not None:
            print(i, end=",")

    print("}")

def helper(arr, subset, index):
    if index == len(arr):
        return print_subset(subset)
    else:
        subset[index] = None
        helper(arr,subset,index+1)
        subset[index] = arr[index]
        helper(arr,subset,index+1)


def find_subsets_iterative(arr: [])->[[]]:
    if len(arr) == 0: return [[]]
    result = [[]]
    for x in arr:
        for i in range(len(result)):
            r = [x] + result[i]
            result.append(r)

    return result

def is_colorful_number(num):
    arr = list(map(int, str(num)))
    unique = {}

    result = find_subsets_iterative(arr)
    result = list(filter(lambda x: x != [], result))
    for each_subset in result:
        product = 1
        for each in each_subset:
            product *= each
        if product in unique:
            return False
        else:
            unique[product] = None

    return True


"""
subset=[1, None]
helper(arr, subset, 3)
"""
'''

Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

Example 1:

Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
6 : 110
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
Example 2:

Input: n = 1
Output: 2
Example 3:

Input: n = 2
Output: 3

0

10 01

101 100 10 

n = 15
counter = 8
set()
i = 0 => 0 -> counter++

1 - addition 
generated_binary_string(0) => 01,10
generated_binary_string(01) => 101
generated_binary_string(10) =>
generated_binary_string(101) =>

0-addition 
generated_binary_string(0) -> 00, 00
generated_binary_string(01) -> 010
g_b_s(10) => 100
g_b_s(010) => 0101, 
g_b_s(100) => 1000, 0100 
g_b_s(0101) => 00101, 01010
g_b_s(1000) => 10000, 01000

if digit_represantation(t) < 15
    counter++
'''

# import requests
# import mysql.connector
# import pandas as pd

from collections import deque


def count_not_cons_one(n):
    if n == 0: return 0
    counter = 0
    queue = deque()
    queue.append("0")
    visited = set()

    while queue:
        str = queue.popleft()

        if bit(str) < n - 1:
            counter += 1

            if str[len(str) - 1] == "1":
                if str + "0" not in visited:
                    queue.append(str + "0")
                    visited.add(str + "0")
            if str[0] == "1":
                if "0" + str not in visited:
                    queue.append("0" + str)
                    visited.add("0" + str)

            if str + "1" not in visited:
                if str[len(str) - 1] != "1":
                    queue.append(str + "1")
                    visited.add(str + "1")

            if "1" + str not in visited:
                if str[0] != "1":
                    queue.append("1" + str)
                    visited.add("1" + str)
    return counter


def bit(str):
    digit = 0
    for i in range(len(str) - 1, -1, -1):
        if str[i] == "1":
            digit += pow(2, len(str) - 1 - i)

    return digit


# print(bit("111"))
print(count_not_cons_one(15))

def find_subsets(arr):
    subset = [None] * len(arr)
    helper(arr,subset,0)

array = [1,2,3]
find_subsets(array)
result = find_subsets_iterative(array)
print(result)


num = 326
print(is_colorful_number(num))
