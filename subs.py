def subs(nums):
    path = []
    result = []
    def backtrack(start):
        result.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
    backtrack(0)
    return result 
print(print(subs([1, 2, 3]))
)