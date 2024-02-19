def find_peak_element(nums):
    n = len(nums)
    left = 0
    right = n - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

# Example usage
nums = [1, 2, 3, 1]
peak_index = find_peak_element(nums)
peak_element = nums[peak_index]
print("Peak element:", peak_element)