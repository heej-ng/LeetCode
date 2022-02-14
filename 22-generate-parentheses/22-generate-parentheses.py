class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(s, n, left, right):
            if left == n and right == n:
                value.append(s)
                return
            if left < n:
                s += "("
                helper(s, n, left+1, right)
                s = s[:-1]
            if left > right:
                s += ")"
                helper(s, n, left, right+1)
        value = []
        helper("", n, 0, 0)
        return value