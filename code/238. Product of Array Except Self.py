class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products_array = [1]*length
        
        # Calculate prefix products
        for i in range(1, length):
            products_array[i] = nums[i-1] * products_array[i-1]
        
        # Calculate suffix products and combine with prefix products
        right_num = nums[-1]
        for i in range(length-2, -1, -1):
            products_array[i] *= right_num
            right_num *= nums[i]
        
        return products_array