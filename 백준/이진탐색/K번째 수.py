def binary_search(start, end):
    output = 0
    while start <= end:
        mid = (start + end) // 2

        count = 0
        for i in range(1, n + 1):
            count += min(mid // i, n)
        if count >= k:
            output = mid
            end = mid - 1
        else:
            start = mid + 1

    return output


if __name__ == "__main__":
    n = int(input())
    k = int(input())

    print(binary_search(1, k))