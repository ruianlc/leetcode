#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
# :date: 2022.10.16
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in list(set(range(0, len(nums))).difference(set([i]))):
                if nums[i] + nums[j] == target:
                    return [i, j]
# @lc code=end

if __name__=="__main__":
    # nums = [2,7,11,15]
    # target = 9
    
    nums = [3,2,4]
    target = 6
    
    result = Solution().twoSum(nums, target)
    print(result)
