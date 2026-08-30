nums = [2, -5, 3, 4, -1, 6, -3]
print("Input Array:", nums)
print()
print("Some subarrays of the input array are:")
for i in range(len(nums)):
    for j in range(i + 1, len(nums) + 1):
        print(nums[i:j])
print()

print("Running sum trace: ")
running = 0
for num in nums:
    running += num
    if running < 0:
        print(f" {num} -> sum = {running} <- negative! RESET to 0")
        running = 0
    else:
        print(f" {num} -> sum = {running}")
print()

running = 0
best = 0
for num in nums:
    running += num
    if running < 0:
        running = 0
    if running > best:
        best = running
print("Array: ", nums)
print("Maximum subarray sum: ", best)
print()
hard = [1, 2, 3, -4, 5, -22, -4, 25, 2, -9]
running = 0
best = 0
for num in hard:
    running += num
    if running < 0:
        running = 0
    if running > best:
        best = running
print("Array: ", hard)
print("Maximum subarray sum: ", best)