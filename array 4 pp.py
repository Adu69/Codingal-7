arr = [1, 3, 5, 2, 2]

# 1. Find total sum
total = 0

for x in arr:
    total = total + x

print("Total sum:", total)


# 2. Find equilibrium point
left_sum = 0
found = False

for i in range(len(arr)):
    right_sum = total - left_sum - arr[i]

    if left_sum == right_sum:
        print("Equilibrium point:", i)
        found = True

    left_sum = left_sum + arr[i]

if found == False:
    print("No equilibrium point")


# 3. Grow a subarray window
window_sum = 0
start = 0

for end in range(len(arr)):
    window_sum = window_sum + arr[end]

    print("Window:", arr[start:end + 1], "Sum:", window_sum)


# 4. Search for a target sum
target = 7
found = False

for i in range(len(arr)):
    sum = 0

    for j in range(i, len(arr)):
        sum = sum + arr[j]

        if sum == target:
            print("Target sum found:", arr[i:j + 1])
            found = True

if found == False:
    print("Target sum not found")