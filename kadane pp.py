arr = [4, -6, 3, 5, -2, 6, -8, 4]

current_sum = arr[0]
best_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = current_sum + arr[i]

    if current_sum < arr[i]:
        current_sum = arr[i]

    if current_sum > best_sum:
        best_sum = current_sum

print("Maximum subarray sum:", best_sum)