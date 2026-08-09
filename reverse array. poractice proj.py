arr = [1, 2, 3, 4, 5]

reverse = []

for i in range(len(arr) - 1, -1, -1):
    reverse.append(arr[i])

print("Reversed array:", reverse)