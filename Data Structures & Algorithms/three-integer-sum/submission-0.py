class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums =sorted(nums)
        valList = []
        for idx, value in enumerate(nums):
            L = idx +1
            R = len(nums) -1
            # skip duplicates
            if idx > 0 and value == nums[idx - 1]:
                continue
            if value > 0:
                break
            while L <R:
                total =  value + nums[L] + nums[R]
                if total >0:
                    R -=1
                elif total <0:
                    L +=1
                else:
                    valList.append([value, nums[L], nums[R]])
                    L +=1
                    R -=1
                    while L< R and nums[L]== nums[L-1]:
                        L +=1
                    while L <R and nums[R] == nums[R+1]:
                        R -=1
        return valList
    
                

        