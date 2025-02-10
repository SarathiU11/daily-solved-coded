
#palindrome
#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x):
        s = str(x)  # Convert number to string
        return s == s[::-1]  # Check if reversed string matches original

# ✅ Run in the same file
sol = Solution()  # Create an instance of the class
print(sol.isPalindrome(121))  # Output: True
print(sol.isPalindrome(-121))  # Output: False
print(sol.isPalindrome(10))  # Output: False
