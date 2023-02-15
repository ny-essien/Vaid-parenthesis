#Given a string s containing just the characters '(',')','{','}','[',']',
#determine if the input string is valid.

#An input string is valid if:

#1. Open brackets must be closed by the same type of brakets.
#2. Open brackets must be closed in the correct order.

#Example 1:
#Input : s = "()"
#Output: true

#Example 2:
#Input: s = "()[]{}"
#Output: true

import unittest

class Solution:

    def is_Valid(self, s : str) -> bool:

        if type(s) is not str:
            raise TypeError("s must be of type str")

        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False

    
class Test_Solution(unittest.TestCase):

    def test_is_Valid(self):
        #making sure that is_Valid returns True for a valid parethensis
        #and returns False for invalid parenthesis

        xgx = Solution()
        s = "()"
        s2 = "()[]{}"
        self.assertIs(xgx.is_Valid(s), True)
        self.assertIs(xgx.is_Valid(s2), True)
        self.assertIs(xgx.is_Valid("()[{}()]"),True)
        self.assertIs(xgx.is_Valid("()[{()}]"),True)

    def test_character_type(self):
        #making sure the s is always of type str

        xgx = Solution()
        self.assertRaises(TypeError, xgx.is_Valid, [1,2,3,4,5])


