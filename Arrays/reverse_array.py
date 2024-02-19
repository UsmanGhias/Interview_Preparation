# Original array
arr = [1, 2, 3, 4, 5]

# Reverse array logic
start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print(arr)
