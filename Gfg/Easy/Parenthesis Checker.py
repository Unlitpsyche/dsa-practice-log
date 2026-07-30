#Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
#An expression is balanced if:
#Each opening bracket has a corresponding closing bracket of the same type. Opening brackets must be closed in the correct order.
#Examples :
#Input: s = "[{()}]"
#Output: true
#Explanation: All the brackets are well-formed.
class Solution:
    def isBalanced(self, s):
        stack = []
        refer = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1]!= refer[c]:
                    return False
                stack.pop()
        return len(stack) == 0