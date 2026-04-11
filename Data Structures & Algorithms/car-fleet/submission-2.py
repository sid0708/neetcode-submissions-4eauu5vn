class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        # closest to the target
        pair.sort(reverse=True)
        stack = []
        for p,s in pair:
            # time it takes (distance/speed)
            stack.append((target-p)/s)
            # pop the last elemnt because stack[-2] is equal
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

        