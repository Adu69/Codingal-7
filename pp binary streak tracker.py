def binary_streak_tracker(arr):
    best = 0
    current = 0

    for num in arr:
        if num == 1:
            current += 1
            if current > best:
                best = current
        else:
            current = 0

    return best


def move_zeros_to_end(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1

    while write < len(nums):
        nums[write] = 0
        write += 1

    return nums



binary = [1, 1, 0, 1, 1, 1, 0, 1]
print("Best streak of 1s:", binary_streak_tracker(binary))

values = [0, 1, 0, 0, 2, 0, 3]
print("Array after moving zeros to the end:", move_zeros_to_end(values))
