class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        # Handle sign
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        result = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            if sign == 1:
                if result > (INT_MAX - digit) // 10:
                    return 0
                # Special case: when result == (INT_MAX - digit) // 10
                if result == (INT_MAX - digit) // 10 and digit > INT_MAX % 10:
                    return 0
            else:
                if result > (-(INT_MIN + digit)) // 10:
                    return 0
                # Special case: when result == (-(INT_MIN + digit)) // 10
                if result > (-(INT_MIN + digit)) // 10 and digit > -(INT_MIN % 10):
                    return 0
            
            result = result * 10 + digit
        
        return result * sign

# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1
    print(f"Input: 123, Output: {sol.reverse(123)}")  # Expected: 321
    
    # Test case 2
    print(f"Input: -123, Output: {sol.reverse(-123)}")  # Expected: -321
    
    # Test case 3
    print(f"Input: 120, Output: {sol.reverse(120)}")  # Expected: 21
    
    # Test overflow cases
    print(f"Input: 1534236469, Output: {sol.reverse(1534236469)}")  # Expected: 0 (overflow)
    print(f"Input: -2147483648, Output: {sol.reverse(-2147483648)}")  # Expected: 0 (overflow)
    print(f"Input: 2147483647, Output: {sol.reverse(2147483647)}")  # Expected: 0 (overflow)
    
    # Edge cases
    print(f"Input: 0, Output: {sol.reverse(0)}")  # Expected: 0
    print(f"Input: 10, Output: {sol.reverse(10)}")  # Expected: 1

test_solution()
