"""
hw2_debugging.py

This module contains an implementation of the merge_sort algorithm,
which is used to sort an array. It also utilizes helper functions
from the `rand` module to generate random arrays.

Functions:
- merge_sort(arr): Sorts the input array using the merge sort algorithm.
- recombine(left_arr, right_arr): Merges two sorted arrays into one.
"""


from rand import random_array


def merge_sort(arr):

    """
    Sorts the input array using the merge sort algorithm.
    Args:
        arr (list): The array to be sorted.
    Returns:
        list: The sorted array.
    """

    if len(arr) <= 1:
        return arr

    half = len(arr)//2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):

    """
    Merges two sorted arrays into one sorted array.

    Args:
        left_arr (list): The first sorted array.
        right_arr (list): The second sorted array.

    Returns:
        list: The merged and sorted array.
    """

    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
        right_index += 1

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]
        left_index += 1

    return merge_arr


inp_arr = random_array([None] * 20)
arr_out = merge_sort(inp_arr)

print(arr_out)
