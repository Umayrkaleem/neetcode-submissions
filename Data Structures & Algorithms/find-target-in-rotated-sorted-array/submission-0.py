class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left<=right:

            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid

            # if we in the left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid +1
                else:
                    right = mid - 1

            # if we in the right sorted portion
            elif nums[right] >= nums[mid]:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1




            




        return -1