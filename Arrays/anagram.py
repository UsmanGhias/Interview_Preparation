def is_anagram(str1, str2):
    # Check if the lengths of the strings are equal
    if len(str1) != len(str2):
        return False
    
    # Create dictionaries to store character counts
    count1 = {}
    count2 = {}
    
    # Count the occurrences of each character in str1
    for char in str1:
        count1[char] = count1.get(char, 0) + 1
    
    # Count the occurrences of each character in str2
    for char in str2:
        count2[char] = count2.get(char, 0) + 1
    
    # Compare the dictionaries
    return count1 == count2


str1 = "listen"
str2 = "silent"

print(is_anagram(str1, str2)) # True


#-----------------Using Simple Python Libraries

# def is_anagram(str1, str2):
#     return sorted(str1) == sorted(str2)

# str1 = "listen"
# str2 = "silent"
# print(is_anagram(str1, str2)) # True