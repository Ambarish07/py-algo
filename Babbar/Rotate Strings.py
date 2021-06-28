class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False
        goal = goal + goal
        return True if s in goal else False
        