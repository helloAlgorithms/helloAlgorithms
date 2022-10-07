class Solution:
    def summaryRanges(self, nums):
        if len(nums) <= 0:
            return []
        start, curr, end = nums[0], nums[0], None
        output = []
        
        for n in nums[1:]:
            curr += 1
            if n == curr:
                end = curr
            else:
                if end == None:
                    output.append(str(start))
                else:
                    output.append(str(start) + "->" + str(end))
                start, curr, end = n, n, None
        if end == None:
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(end))
        return output


# other version
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []     
        cur_idx = 0 
        
        while cur_idx < len(nums): 
            start = cur_idx  
            while cur_idx < len(nums) - 1 and nums[cur_idx] + 1 == nums[cur_idx + 1]: 
                cur_idx += 1 
            
            if cur_idx != start: 
                res.append(str(nums[start]) + "->" + str(nums[cur_idx]))
            else: 
                res.append(str(nums[cur_idx]))
            
            cur_idx += 1
        return res
		