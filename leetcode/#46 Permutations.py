class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, path, ret):
        if not nums:
            ret.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], ret)

#     def permute(self, nums):
#         if len(nums) <= 1:
#             return [nums]
#         ret = []
#         for i, num in enumerate(nums):
#             n = nums[:i] + nums[i+1:]
#             dfs = self.permute(n)
#             for y in dfs:
#                 ret.append([num]+y)
#         return ret
