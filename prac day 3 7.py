def permute_unique(nums):
    def backtrack(start):
        if start == len(nums):
            permutations.append(nums[:])
            return
        seen = set()
        for i in range(start, len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    
    permutations = []
    backtrack(0)
    return permutations

nums = [1, 1, 2]
print("Unique permutations:", permute_unique(nums))
