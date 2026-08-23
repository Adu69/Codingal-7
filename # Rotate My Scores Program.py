# Rotate My Scores Program

scores = [10, 20, 30, 40, 50, 60, 70]

print("Original scores:", scores)


# 1. Reverse scores using two pointers
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        left = left + 1
        right = right - 1

    return arr


# 2. Reverse elements in fixed-size groups
def reverse_groups(arr, k):
    i = 0

    while i < len(arr):
        left = i
        right = i + k - 1

        # Make sure right does not go outside the list
        if right >= len(arr):
            right = len(arr) - 1

        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            left = left + 1
            right = right - 1

        i = i + k

    return arr


# 3. Left rotation by 1
def left_rotate_one(arr):
    first = arr[0]

    i = 0
    while i < len(arr) - 1:
        arr[i] = arr[i + 1]
        i = i + 1

    arr[len(arr) - 1] = first

    return arr


# 4. Left rotation by n
def left_rotate_n(arr, n):
    n = n % len(arr)

    count = 0

    while count < n:
        left_rotate_one(arr)
        count = count + 1

    return arr


# 5. Find leaders by scanning from the right
def find_leaders(arr):
    leaders = []

    # The last element is always a leader
    max_value = arr[len(arr) - 1]
    leaders.append(max_value)

    i = len(arr) - 2

    while i >= 0:
        if arr[i] > max_value:
            leaders.append(arr[i])
            max_value = arr[i]

        i = i - 1

    # Reverse leaders so they appear in original order
    reverse_array(leaders)

    return leaders


# Testing the functions

print("\n1. Reverse:")
a = [10, 20, 30, 40, 50, 60, 70]
print(reverse_array(a))


print("\n2. Reverse in groups of 3:")
a = [10, 20, 30, 40, 50, 60, 70]
print(reverse_groups(a, 3))


print("\n3. Left rotation by 1:")
a = [10, 20, 30, 40, 50, 60, 70]
print(left_rotate_one(a))


print("\n4. Left rotation by 2:")
a = [10, 20, 30, 40, 50, 60, 70]
print(left_rotate_n(a, 2))


print("\n5. Leaders:")
a = [16, 17, 4, 3, 5, 2]
print(find_leaders(a))