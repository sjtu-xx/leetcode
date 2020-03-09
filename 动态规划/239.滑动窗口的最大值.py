# 采用双端队列实现
#from collections import deque
#class Solution:
#    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
#        """
#        最大堆 采用双端队列实现
#        二叉树
#        """
#        n = len(nums)
#        if n * k == 0:
#            return []
#        if k == 1:
#            return nums
#        
#        def clean_deque(i):
#            if deq and deq[0] == i - k:
#                deq.popleft()
#
#            while deq and nums[i] > nums[deq[-1]]:
#                deq.pop()
#        
#        deq = deque()
#        max_idx = 0
#        result = []
#        for i in range(k):
#            clean_deque(i)
#            deq.append(i)
#
#            if nums[i] > nums[max_idx]:
#                max_idx = i
#        result.append(nums[max_idx])
#        
#        for i in range(k,n):
#            clean_deque(i)
#            deq.append(i)
#
#            result.append(nums[deq[0]])
#        return result


# 动态规划
# 建立left和right数组
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        """
        最大堆 采用双端队列实现
        二叉树
        """
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        left = [None] * n
        right = [None] * n
        left[0] = nums[0]
        right[-1] = nums[-1]

        for i in range(1,n):
            # 对left中的数据进行修改
            if i % k == 0:
                left[i] = nums[i]
            else:
                if nums[i] < left[i-1]:
                    left[i] = left[i-1]
                else:
                    left[i] = nums[i]
            
            j = n - 1 - i
            # 对right中的数据进行修改
            if j % k == k-1:
                right[j] = nums[j]
            else:
                if nums[j] < right[j+1]:
                    right[j] = right[j+1]
                else:
                    right[j] = nums[j]

        return  [max(right[i],left[i+k-1]) for i in range(n-k+1)]
                


