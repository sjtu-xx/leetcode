from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        首先，可以先进行一次遍历，将逆序的数字修改为可能的最小值，
        第二次遍历如果存在逆序则返回False
        """
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if i == 0:
                    nums[0] = nums[1]
                elif nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                break
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return False
        return True


