class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        counter = 0
        highest = 0
        for n in nums:
            if (n-1) not in setNums:
                counter = 0
                while (n+counter) in setNums:
                    counter += 1
                    if counter > highest:
                        highest = counter
            
        return highest
        
