def findLeaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(arr[i])
    
    return leaders[::-1]
print(findLeaders([16, 17, 4, 3, 5, 2]))       # [17, 5, 2]
print(findLeaders([1, 2, 3, 4, 0]))           # [4, 0]
print(findLeaders([7, 10, 4, 10, 6, 5, 2]))   # [10, 6, 5, 2]
print(findLeaders([5]))                       # [5]
print(findLeaders([100, 50, 20, 10]))         # [100, 50, 20, 10]
print(findLeaders(list(range(1, 1000001))))   # [1000000]
