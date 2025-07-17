class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # Single digit numbers are palindromes
        if x < 10:
            return True
        
        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x % 10 == 0:
            return False
        
        # Reverse half the number and compare with the other half
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even number of digits: x == reversed_half
        # For odd number of digits: x == reversed_half // 10
        # (because reversed_half has the extra middle digit)
        return x == reversed_half or x == reversed_half // 10

def test_solution():
    sol = Solution()
    test_cases = [121, -121, 10, 0, 1, 12321, 12345, 1001, 1234321]
    
    print("Mathematical approach:")
    for x in test_cases:
        result = sol.isPalindrome(x)
        print(f"Input: {x}, Output: {result}")

test_solution()
        
