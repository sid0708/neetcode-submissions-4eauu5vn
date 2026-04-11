class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftpre = [0] * len(nums)
        rightpre = [0] * len(nums)
        # insert 1 in left and right most spots
        leftpre[0] = 1
        rightpre[-1] = 1
        prod1 = 1
        prod2 = 1
        result =[]
        # now multiply
        for i in range(1, len(nums)):
    #         print(prod1,lst[i-1] ) # prod1 will always be 1 and lst[i-1] is [1,2,3] when the input is [1,2,3,4]
            prod1 = prod1 * nums[i-1]
            leftpre[i] = prod1 # insert it into the leftpre

        for i in range(len(leftpre)-2,-1,-1):
            prod2 = prod2 * nums[i+1]
            rightpre[i]  = prod2
        
        for i in range(0, len(nums)):
            result.append(leftpre[i]*rightpre[i])
        return result
    

        

        

        