def per(nums):
    result = []
    path = []
    used = [False] * len(nums)
    def backtrack():
        if len(path) == len(nums):
            result.append(path[:])
            return 
        for i in range(len(nums)):
            if used[i]:
                continue 
            path.append(nums[i])
            used[i] = True
            backtrack()
            used[i] = False
            path.pop()
    backtrack()
    return result
print(per([1, 2, 3]))