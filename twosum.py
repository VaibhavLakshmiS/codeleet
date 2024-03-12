class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}
        ind=0
        for i in nums:
            wanted = target - i
            if wanted in h :
                return [h[wanted],ind]
            h[i]=ind
            ind+=1
        return []