def num_identical_pairs(nums):
    count = {}
    good_pairs = 0
    
    for num in nums:
        if num in count:
            good_pairs += count[num]
            count[num] += 1
        else:
            count[num] = 1
    
    return good_pairs

nums = [1, 2, 3, 1, 1, 3]
print("Number of good pairs:", num_identical_pairs(nums))
