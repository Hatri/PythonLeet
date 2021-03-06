'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

class Solution:
    def deCoding(self, letter: string) -> int:
        previousNumberWays = 0
        numberOfWays = int(letter > '')
        previousDigit = ''
    
        for digit in letter:
            copyPrevious = previousNumberWays
            previousNumberWays = numberOfWays

            numberOfWays = (digit > '0') * numberOfWays
            numberOfWays += (9 < int(previousDigit + digit) < 27) * copyPrevious
            previousDigit = digit

        return numberOfWays 