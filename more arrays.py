binary = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
streak = 0
for num in binary:
    if num == 0:
        streak = 0
    else:
        streak += 1

    print(num, "->", streak)
print()

streak = 0
best = 0
for num in binary:
    if num == 0:
        streak = 0
    else:
        streak += 1
        best = streak

print("Best Streak:", best) 
print("max consecutive is: ", best)
print()

nums = [1, 0, 3, 6, 0, 0, 0, 2, 355, 0, 72]
print("Before", nums)
zero = 0
for nonzero in range (len(nums)):
    if nums[nonzero] != 0:
        nums[zero], nums[nonzero] = nums[nonzero], nums[zero]
        zero += 1
print("After", nums)
print()

print("After: ", nums)
print()

print("Write pointer stopped at:", zero)
print("Non-zeros at front: ", zero)
print("Zeros at end: ", len(nums) - zero)
