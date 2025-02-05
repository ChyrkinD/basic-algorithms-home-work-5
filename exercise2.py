def binary_search(arr : list, x : float) -> tuple:
    arr.sort()
    low = 0
    high = len(arr)-1
    mid = 0
    uppper_bound = 0
    iteration_count = 0
    while low <= high:
        iteration_count += 1
        mid = (low + high) // 2

        if arr[mid] == x:
            return iteration_count, arr[mid]
        elif arr[mid] < x:
            low = mid + 1
        else:
            uppper_bound = arr[mid]
            high = mid - 1
    
    return iteration_count, uppper_bound

def main():
    arr = [3.14, 5.01, 1.9, 2.8, 9.87]
    x = 2.8
    result = binary_search(arr,x)
    print(result)

if __name__ == '__main__':
    main()