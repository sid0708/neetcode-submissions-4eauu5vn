class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        # sort by closest to the target
        pair.sort(reverse=True)
        stack = []
        for p,s in pair:
            stack.append((target-p)/s)
        # now stack contains the speed
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                # behind car reaches first than the one ahead 
                stack.pop()
        return len(stack) # distinct car


        