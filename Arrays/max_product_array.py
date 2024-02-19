def max_product_array(arr):
    if len(arr) < 2:
        return None

    max_product = arr[0] * arr[1]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
    return max_product

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(max_product_array(arr)) # 20
