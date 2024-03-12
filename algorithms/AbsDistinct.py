'''
A non-empty array A consisting of N numbers is given. 
The array is sorted in non-decreasing order.
The absolute distinct count of this array
is the number of distinct absolute values
among the elements of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6


The absolute distinct count of this array is 5, 
because there are 5 distinct absolute values among the elements of this array,
namely 0, 1, 3, 5 and 6
'''


''''
def absolute_value(value):
    if value < 0 :
        return value * -1
    return value

test_list = [-5, -3, -1, 0, 3, 6]


abs_list = []
for elem in test_list:
    abs_list.append(absolute_value(elem))
print(abs_list)
'''

unique_elememts = set()
def solution(elems_array: list):
    for elem in elems_array:
        unique_elememts.add(abs(elem))
    return len(unique_elememts)

example_array = [-5,-3,-3,0,3,6]

# print(solution(example_array))