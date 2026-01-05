def merge_sort(a, b):
    concat_data = a + b
    sorted_data = sorted(concat_data)
    return sorted_data


bsg = merge_sort([3, 1], [5, 2])
print(bsg)


def merge_and_sort(a, b):
    return sorted(a + b)


c = merge_and_sort([2, 76], [5, 255])
print(c)
