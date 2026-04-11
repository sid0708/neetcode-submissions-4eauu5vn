class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # initialize with the start and break when it's equal
        slow, fast = nums[0], nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        # reset the slow again
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        