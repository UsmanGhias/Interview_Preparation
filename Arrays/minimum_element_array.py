def find_minimum(arr):
    minimum = float('inf')
    for num in arr:
        if num < minimum:
            minimum = num
    return minimum, arr

# Example usage
user_input = input("Enter numbers separated by commas: ")
my_array = [int(n) for n in user_input.split(',')]

minimum, array = find_minimum(my_array)
print("Minimum element:", minimum)
print("Array:", array)
    