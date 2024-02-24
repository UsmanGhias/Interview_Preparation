def left_rotation(arr, left):
    n = len(arr)
    left = left % n # if left is greater than n
    rotated_arr = arr[left:] + arr[:left]
    return rotated_arr

def right_rotation(arr, right):
    n = len(arr)
    right = right % n # if right is greater than n
    rorate_arr = arr[n - right:] + arr[:n - right]
    return rorate_arr


arr = [1, 2, 3, 4, 5]
left = 2
print(left_rotation(arr, left)) # [3, 4, 5, 1, 2]
print(right_rotation(arr, left)) # [4, 5, 1, 2, 3]