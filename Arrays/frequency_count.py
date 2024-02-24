def frequency_count(arr):
    frequency = {}
    
    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(frequency_count(arr)) # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}