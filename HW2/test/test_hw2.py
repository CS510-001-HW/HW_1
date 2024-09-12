
from src.hw2_debugging import merge_sort
print("Test file is being executed.")


# Test case 1: Testing an already sorted array
def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]


# Test case 2: Testing an array with random integers

def test_unsorted_array():
    arr = [5, 3, 8, 1, 2]
    assert merge_sort(arr) == [1, 2, 3, 5, 8]


# Test case 3: Testing an array with duplicate elements

def test_array_with_duplicates():
    arr = [4, 1, 3, 4, 2]
    assert merge_sort(arr) == [1, 2, 3, 4, 4]

# Add more test cases as needed
