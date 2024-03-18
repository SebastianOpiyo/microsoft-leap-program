def two_sum(arr, target):
    '''
    Given a sorted array, find a pair elements whose sum equals a given target.
    '''
    left, right = 0, len(arr)-1
    current_sum = 0 
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    # there no existence
    return -1 

nums = [2, 7, 11, 15]
target = 9

# print(two_sum(nums, target))


# Three sum problem
def three_sum(arr, target):
    '''
    Given an array find a triplet that equals the target.
    '''
    left = 0
    right = len(arr)-1
    current_sum = 0

    for i in range(len(arr)-1):
        current_sum = arr[i] + arr[left] + arr[right]
        if current_sum == target:
            return [i, left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return -1



nums = [-1, 2, 1, -4]
target = 1
print(three_sum(nums, target))

