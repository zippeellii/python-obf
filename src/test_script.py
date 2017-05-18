# Sum of all elements in array
def sum_of_array(arr):
    return reduce(lambda x, y: x + y, arr)

# Define array
lst = [1,2,3,4,5]

sum = sum_of_array([1,2,3,4])

def print_a_string(string):
    print string

print 'The sum from sum_of_array of elements in list is', sum
print 'The reversed order of elements in list is', lst[::-1]
print_a_string('Hello World!')

a = 5

b = 7

c = a+b

print '5+7=12. 12 should therefore show on the following line'
print c

