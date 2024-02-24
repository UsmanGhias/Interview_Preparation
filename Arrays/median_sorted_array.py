def median_sorted_array(arr1, arr2):
    merged_arr = []
    i , j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_arr.append(arr2[j])
        j += 1
    
    if len(merged_arr) % 2 == 0:
        return (merged_arr[len(merged_arr) // 2] + merged_arr[len(merged_arr) // 2 - 1]) / 2
    else:
        return merged_arr[len(merged_arr) // 2]


num1 = [1, 3]
num2 = [4, 5]

print(median_sorted_array(num1, num2))

    