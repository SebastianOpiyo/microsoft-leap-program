'''
Problem Statement: Suppose we have an array of integers, and we want to find the maximum length of a subarray with unique elements. In other words, we want to identify the longest contiguous subarray where no number repeats.

Example: Consider the input array: [1, 2, 3, 1, 2, 3, 4, 5].

The maximum length of a subarray with unique elements is 5, corresponding to the subarray [1, 2, 3, 4, 5].
'''


def find_max_length_subarray(arr):
    window_sum = 0
    window_start = 0
    max_length = 0
    unique_elements = set()

    for window_start in range(len(arr)):
        window_sum += arr[window_start]
        unique_elements.add(arr[window_start])
        print(unique_elements)
 
        while arr[window_start] not in unique_elements and window_start <= range(len(arr)):
            window_sum += arr[window_start, window_start + 1]
            max_length += 1
        window_start += 1
    return max_length

print(find_max_length_subarray([1, 2, 3, 1, 2, 3, 4, 5]))

def find_num_sliding_windows(arr:list, array_size:int):
    '''Given an array and a fixed size of a sliding window,
    find the max number of sliding windows that can be achived.'''
    num_sliding_windows  = 0
    start = 0
    end = len(arr)-1

    for i in range(end):
        while start <= end:
            
