# Sum of all elements in array
def sum_of_array(arr):
    return reduce(lambda x, y: x + y, arr)

# Define array
lst = [1,2,3,4,5]

sum = sum_of_array([1,2,3,4])

print 'The reversed order of elements in list is', lst[::-1]

