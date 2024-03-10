class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}  # create a hashmap 
        ind=0  # to get the correct indices
        for i in nums: # traverse through the nums array 
            wanted = target -i  # find the value to search in the hashmap 
            if wanted in h:    # check if the value is in hashmap
                return [h[wanted],ind] # get the indices
            h[i]=ind # store the current element and its index in the hash map
            ind+=1 # increment the index and move to the next index
        return [] # not found then return empty 