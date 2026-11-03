import random

# Deterministic Quick Sort
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


# Randomized Quick Sort
def random_quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = []
    right = []
    equal = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)

    return random_quick_sort(left) + equal + random_quick_sort(right)


# Main Program
arr = list(map(int, input("Enter numbers: ").split()))

print("Original Array:", arr)
print("Deterministic Sort:", quick_sort(arr))
print("Randomized Sort:", random_quick_sort(arr))
