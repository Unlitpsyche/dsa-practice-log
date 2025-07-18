class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
        # If the character is a closing bracket
            if char in mapping:
            # Pop the top element from the stack if it's not empty; otherwise assign dummy value '#'
                top_element = stack.pop() if stack else '#'

            # If the mapping for the closing bracket doesn't match the top element, return False
                if mapping[char] != top_element:
                    return False
            else:
            # It's an opening bracket, push to stack
                stack.append(char)

    # If the stack is empty, all brackets matched correctly
        return not stack
    
