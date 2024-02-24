def max_water_problem(arr):
    max_water = 0
    left, right = 0, len(arr) - 1
    
    while left < right:
        h = min(arr[left], arr[right])
        w = right - left
        current_water = h * w
        
        max_water = max(max_water, current_water)
        
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_water


arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_water_problem(arr)) # 49