def findLeaders(arr, n):
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    leaders.reverse()
    return leaders

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = findLeaders(arr, n)
    print(*result)
