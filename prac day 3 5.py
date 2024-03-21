def min_jumps_to_reach_end(nums):
    if len(nums) <= 1:
        return 0
    
    if nums[0] == 0:
        return -1  
    
    jumps = 1  
    max_reach = nums[0]  
    current_end = nums[0]  
    
    for i in range(1, len(nums)):
        if i == len(nums) - 1:
            return jumps  
        
        max_reach = max(max_reach, i + nums[i]) 
        
        if i == current_end:  
            jumps += 1  
            current_end = max_reach  
            
            if current_end <= i:
                return -1 
    
    return -1 

nums = [2, 3, 1, 1, 4]
print("Minimum number of jumps:", min_jumps_to_reach_end(nums))
