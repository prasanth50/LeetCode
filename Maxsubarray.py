# 

def maxsubarray(nums): // Function to define Max subarray.

    maxsum = nums[0]
    cur_sum = 0

    for i in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += i
        maxsum = max(maxsum,cur_sum)
    return maxsum

print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxsubarray([-1,2])) 
