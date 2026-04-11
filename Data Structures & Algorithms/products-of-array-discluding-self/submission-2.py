class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Lprefix = [1] * len(nums)
        Rsuffix = [1] *len(nums)
        result = [1] *len(nums)
        for i in range(1,len(nums)):
            Lprefix[i] = nums[i-1] * Lprefix[i-1]
        for j in range(len(nums)-2, -1, -1):
            Rsuffix[j] = nums[j+1] * Rsuffix[j+1]
        print(Lprefix,Rsuffix)
        for i in range(len(nums)):
            result[i] = Lprefix[i] * Rsuffix[i]
        return result
        
       

            

            

    

        

        

        