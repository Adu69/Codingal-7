def print2ndlargest(arr, arr_size):
    first = second = float('-inf')
    for i in range(arr_size):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    if second == float('-inf'):
        print("There is no second largest element")
    else:
        print("The second largest element is:", second)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a_size = len(a)
print2ndlargest(a, a_size)
