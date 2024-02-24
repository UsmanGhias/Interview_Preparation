def merge_sorted_array(arr1, arr2):
    merged_array = []
    i, j , = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1
    return merged_array

arr1 = [1, 3, 4, 5]
arr2 = [2, 6, 7, 8]
print(merge_sorted_array(arr1, arr2))