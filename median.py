array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]

print("Array 1: ", array1)
print("Array 2: ", array2)
length =  len(array1) + len(array2)
print("Combined Array Length: ", length)
both_arrays = array1 + array2
print("Combined Array: ", both_arrays)
print("Length of Combined Array: ", len(both_arrays))
if len(both_arrays) / 2 == 0:
    median = (both_arrays[len(both_arrays) // 2 - 1] + both_arrays[len(both_arrays) // 2]) / 2
else:
    median = both_arrays[len(both_arrays) // 2]
print("Median of Combined Array: ", median)