arr = [2, 4, 1, 3, 2, 5, 1]
target = 6

print("Array:", arr)

total_sum = sum(arr)
print("Total sum:", total_sum)

print("\nLeft-Right Balance:")

for i in range(len(arr)):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i + 1:])
    print("Position", i, ": Left =", left_sum, "Right =", right_sum)

print("\nEquilibrium Point:")

equilibrium = -1

for i in range(len(arr)):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i + 1:])

    if left_sum == right_sum:
        equilibrium = i
        break

if equilibrium != -1:
    print("Equilibrium point is at index", equilibrium)
    print("Value:", arr[equilibrium])
else:
    print("No equilibrium point found")

print("\nGrowing Subarray Window:")

for end in range(1, len(arr) + 1):
    window = arr[:end]
    print("Window:", window, "Sum:", sum(window))

print("\nTarget Sum Search:")

found = False

for start in range(len(arr)):
    current_sum = 0

    for end in range(start, len(arr)):
        current_sum += arr[end]

        if current_sum == target:
            print("Subarray found:", arr[start:end + 1])
            print("Indexes:", start, "to", end)
            found = True
            break

        if current_sum > target:
            break

    if found:
        break

if not found:
    print("No subarray with target sum found")