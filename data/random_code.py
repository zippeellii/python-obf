def quick_sort(arr, first, last):
    """ Quicksort
        Complexity: best O(n) avg O(n log(n)), worst O(N^2)
    """
    if first < last:
        pos = partition(arr, first, last)
        print(arr[first:pos-1], arr[pos+1:last])
        # Start our two recursive calls
        quick_sort(arr, first, pos-1)
        quick_sort(arr, pos+1, last)

def partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]: # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    print(wall)
    return wall

def merge_sort(arr):
    """ Merge Sort
        Complexity: O(n log(n))
    """
    # Our recursive base case
    if len(arr)<= 1:
        return arr
    mid = len(arr)/2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[mid:]), merge_sort(arr[:mid])

    # Merge each side together
    return merge(left, right)

def merge(left, right):
    """ Merge helper
        Complexity: O(n)
    """
    arr = []
    left_cursor, right_cursor = 0,0
    while left_cursor < len(left) and right_cursor < len(right):
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            arr.append(left[left_cursor])
            left_cursor+=1
        else:
            arr.append(right[right_cursor])
            right_cursor+=1
   # Add the left overs if there's any left to the result
    for i in range(left_cursor,len(left)):
        arr.append(left[i])
    for i in range(right_cursor,len(right)):
        arr.append(right[i])

   # Return result
    return arr

def spiral_traversal(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end+1):
            res.append(matrix[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end+1):
            res.append(matrix[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for i in range(col_end, col_begin-1, -1):
                res.append(matrix[row_end][i])
        row_end -= 1

        if col_begin <= col_end:
            for i in range(row_end, row_begin-1, -1):
                res.append(matrix[i][col_begin])
        col_begin += 1

    return res

def wiggle_sort(nums):
    for i in range(len(nums)):
        if (i % 2 == 1) == (nums[i-1] > nums[i]):
            nums[i-1], nums[i] = nums[i], nums[i-1]
