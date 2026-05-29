class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0 
        right = len(nums)-1

        while left <= right:
            mid = (left + right )// 2 #get mid of array
            if nums[mid] == target: #find!
                return mid
            if target < nums[mid]: 
                right = mid -1 #remove all right
            else:
                left = mid + 1 

        return -1 
        