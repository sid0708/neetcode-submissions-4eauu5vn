class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.helper(1, [],combs, n,k)
        return combs
    def helper(self, i, currcombs, combs, n, k):
        if len(currcombs) == k:
            combs.append(currcombs.copy())
            return
        if i > n:
            return
        # include i
        currcombs.append(i)
        self.helper(i+1, currcombs, combs, n, k)
        currcombs.pop()
        self.helper(i+1, currcombs, combs, n,k)

        