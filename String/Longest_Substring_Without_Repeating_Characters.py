class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        left = 0
        max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            # Shrink window from left until no duplicates
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character to window
            char_set.add(s[right])
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length

solution = Solution()
print("Input: 'abcabcbb'")
print(f"Result: {solution.lengthOfLongestSubstring('abcabcbb')}")
print("Input: 'pwwkew'")
print(f"Result: {solution.lengthOfLongestSubstring('pwwkew')}") 
