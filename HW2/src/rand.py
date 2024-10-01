"""
rand.py

This module provides a function to generate a random array of integers
using the `shuf` command-line utility. The function fills the given array
with randomly shuffled numbers in the range from 1 to 20.


Functions:
- random_array(arr): Fills the provided array with random integers
  from 1 to 20.
"""

import subprocess


def random_array(arr):
    """
    This function uses the `shuf` command-line utility to generate random
    numbers. It replaces each element in the input array with a new random
    number.

    Args:
        arr (list): A list to be filled with random integers. The list should
                    have a length defined by the caller.

    Returns:
        list: The input list filled with random integers from 1 to 20.
    """
    for i, _ in enumerate(arr):
        try:
            shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
            arr[i] = int(shuffled_num.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")
            arr[i] = None
    return arr
