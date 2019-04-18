class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        self.dfs(nums, [], ret)
        return ret
        
    # 2000ms
    # def dfs(self, nums, path, ret):
    #     if not nums:
    #         ret.append(path)
    #     for i, num in enumerate(nums):
    #         n = nums[:i] + nums[i+1:]
    #         if path+[num] in ret:
    #             continue
    #         else:
    #             self.dfs(n, path+[num], ret)
    
    # 70ms
    def dfs(self, nums, path, ret):
        if not nums:
            ret.append(path)
        for i in range(len(nums)):
            n = nums[:i] + nums[i+1:]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(n, path+[nums[i]], ret)
