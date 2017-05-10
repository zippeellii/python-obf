def quick_sort(arr, first, last):
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
    # Our recursive base case
    if len(arr)<= 1:
        return arr
    mid = len(arr)/2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[mid:]), merge_sort(arr[:mid])

    # Merge each side together
    return merge(left, right)

def merge(left, right):
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

def backtrack(pattern, string, dic):
    print(dic)
    if len(pattern) == 0 and len(string) > 0:
        return False
    if len(pattern) == len(string) == 0:
        return True
    for end in range(1, len(string)-len(pattern)+2):
        if pattern[0] not in dic and string[:end] not in dic.values():
            dic[pattern[0]] = string[:end]
            if backtrack(pattern[1:], string[end:], dic):
                return True
            del dic[pattern[0]]
        elif pattern[0] in dic and dic[pattern[0]] == string[:end]:
            if backtrack(pattern[1:], string[end:], dic):
                return True
    return False

def shortest_distance(grid):
    if not grid or not grid[0]:
        return -1

    matrix = [[[0,0] for i in range(len(grid[0]))] for j in range(len(grid))]

    count = 0    # count how many building we have visited
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                bfs(grid, matrix, i, j, count)
                count += 1

    res = float('inf')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j][1]==count:
                res = min(res, matrix[i][j][0])

    return res if res!=float('inf') else -1

def bfs(grid, matrix, i, j, count):
    q = [(i, j, 0)]
    while q:
        i, j, step = q.pop(0)
        for k, l in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            # only the position be visited by count times will append to queue
            if 0<=k<len(grid) and 0<=l<len(grid[0]) and \
                    matrix[k][l][1]==count and grid[k][l]==0:
                matrix[k][l][0] += step+1
                matrix[k][l][1] = count+1
                q.append((k, l, step+1))

def bracket(words, symbols):
    root = TrieNode()
    for s in symbols:
        t = root
        for char in s:
            if char not in t.c:
                t.c[char] = TrieNode()
            t = t.c[char]
        t.sym = s
    result = dict()
    for word in words:
        i = 0
        symlist = list()
        while i < len(word):
            j, t = i, root
            while j < len(word) and word[j] in t.c:
                t = t.c[word[j]]
                if t.sym is not None:
                    symlist.append((j+1-len(t.sym), j+1, t.sym))
                j += 1
            i += 1
        if len(symlist) > 0:
            sym = reduce(lambda x, y: x if x[1]-x[0] >= y[1]-y[0] else y, symlist)
            result[word] = "{}[{}]{}".format(word[:sym[0]], sym[2], word[sym[1]:])
    return tuple(word if word not in result else result[word] for word in words)

def serialize(root):
    def build_string(node):
        if node:
            vals.append(str(node.val))
            build_string(node.left)
            build_string(node.right)
        else:
            vals.append("#")
    vals = []
    build_string(root)
    return " ".join(vals)


def deserialize(data):
    def build_tree():
        val = next(vals)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = build_tree()
        node.right = build_tree()
        return node
    vals = iter(data.split())
    return build_tree()

def count_elem(array, query):
    def first_occurance(array, query):
        lo, hi = 0, len(array) -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (array[mid] == query and mid == 0) or \
                (array[mid] == query and array[mid-1] < query):
                return mid
            elif (array[mid] <= query):
                lo = mid + 1
            else:
                hi = mid - 1
    def last_occurance(array, query):
        lo, hi = 0, len(array) -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (array[mid] == query and mid == len(array) - 1) or \
                (array[mid] == query and array[mid+1] > query):
                return mid
            elif (array[mid] <= query):
                lo = mid + 1
            else:
                hi = mid - 1

    first = first_occurance(array, query)
    last = last_occurance(array, query)
    if first is None or last is None:
        return None
    return last - first + 1
