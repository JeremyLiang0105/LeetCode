class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                k = j + 1
                r = len(nums) - 1
                while k < r:
                    if nums[i] + nums[j] + nums[k] + nums[r] == target and [nums[i], nums[j], nums[k], nums[r]] not in res:
                        res.append([nums[i], nums[j], nums[k], nums[r]])
                        k += 1 
                        r -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[r] > target:
                        r -= 1
                    else:
                        k += 1
        return res
    
    # time complexity: O(n^3)
    # space complexity: O(n)
