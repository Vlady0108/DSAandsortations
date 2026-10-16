# When needed a stable sorting algorithms
# most appropriate is merge sort
# In a large production system, it is more like
# usable the quick sort


# Insertion Sort 1
# compare each element with the previous ones
# and insert it in the correct position
# or compare with the left element ( or neighbor)
# Compplexity is O(n^2)
#
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
    return a


# Insertion Sort 2
# Complexity is O(n^2)
# Insertion sort complexity for pre-sorted
# array is O(n) and uses the least memory

def insertion_sort2(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums

a = [5, 2, 4, 6, 1, 3]
print(insertion_sort(a))
print(insertion_sort2(a))

# Bubble Sort
# compare adjacent elements and swap if necessary

def bubble_sort(a):
    n = len(a)
    for p in range(n - 1):
        swapped = False
        for i in range(n - 1 - p):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
    return a

a = [5, 2, 4, 6, 1, 3]
print(bubble_sort(a))

# Bubble Sort 2
# O(n^2)
# at best O(n) at worst O(n^2)
# good for studying algorithms

def bubble_sort2(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i -1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return nums

a = [5, 2, 4, 6, 1, 3]
print(bubble_sort2(a))
# Comb Sort
# Gap-based sorting
# or compare with the element at the gap

def comb_sort(a):
    n = len(a); g = n
    while True:
        g = max(1, int(g / 1.3))
        swapped = False
        for i in range(n - g):
            if a[i] > a[i + g]:
                a[i], a[i + g] = a[i + g], a[i]
                swapped = True
        if g == 1 and not swapped: break
    return a

a = [5, 2, 4, 6, 1, 3]
print(comb_sort(a))



# Selection Sort
# compare with current minimum
def selection_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a


a = [5, 2, 4, 6, 1, 3]
print(selection_sort(a))


# Merge sort:
# O(n log n)
# merge sort is a good idea when we need a
# fast sorting algorithm and memory is not a concern
# Merge_sort :
# is a recursive algorithm
# is faster than insertion sort
# uses divide and conquer algorithm

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    l = merge_sort(nums[:mid])
    r = merge_sort(nums[mid:])
    return merge(l, r)

def merge(first, second):
    result = []
    i = j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            result.append(first[i])
            i += 1
            continue
        result.append(second[j])
        j += 1
    while i < len(first):
        result.append(first[i])
        i += 1
    while j < len(second):
        result.append(second[j])
        j += 1
    return result

a = [3 , 2, 1, 6, 5, 4]
print(merge_sort(a))


# Quick sort :

# Fast and efficient
# Uses divide and conquer algorithm - recursive ( also known as partition-exchange sort )

# A lot of good algorithms are divide and conquer algorithms
# An already sorted list causes quick sort to
# break down in complexity to O(n^2)
# Worst case complexity: O(n^2)
# Best case complexity: O(n log n)

# median-of-three approach is sometimes used
# because it does not require randomization
# and impurity is avoided

def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i

a = [3, 2, 1, 6, 5, 4]
# quick_sort(a) - this will not work
# as the function is not returning anything
# Thus, 2 missing positional arguments are needed
#  as a low and high index like so:

quick_sort(a, 0, len(a) - 1)
print(a)



# Reduction to P or the fibonacci sequence
# Solution 1:
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
print(fib(10))

# Solution 2:

def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    current = 0
    parent = 1
    grandparent = 0
    for i in range(0, n - 1):
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current
print(fib2(10))


# Exponential time algorithm
#

def power_set(input_set):
    if len(input_set) == 0:
        return [[]]
    subset = []
    first = input_set[0]
    remaining = input_set[1:]
    remaining_subsets = power_set(remaining)
    for subset in remaining_subsets:
        subset.append([first] + subset)
        subsets.append(subset)
    return subsets


# The following function complexity is O(1):

def get_name_at_index(names, i):
    return names[i]

# The following function complexity is O(log n):

def naive_log2(x):
    count = 0
    while x > 1:
        x /= 2
        count += 1
    return count

# halvedSections returns a list of lists.
# For example, n = 12 results in:
# [
#  [0 1 2 3 4 5 6 7 8 9 10 11 12]
#  [0 1 2 3 4 5 6]
#  [0 1 2 3]
#  [0 1]
# ]

# En equivalent ( but not fully reduced ) way to
# express the complexity is O(2n)
# and the most reduced form of this function complexity
# is O(n)

def halvedSections(n):
    rows = []
    i = n
    while i > 0:
        col = []
        for j in range(i + 1):
            col.append(j)
        rows.append(col)
        i //= 2
    return rows

print(halvedSections(12))
