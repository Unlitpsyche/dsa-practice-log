#Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.).
#Note: The string may contain leading or trailing dots(.) or multiple dots(.) between two words. The returned string should only have a single dot(.) separating the words, and no extra dots should be included.
#Examples :
#Input: s = "i.like.this.program.very.much"
#Output: "much.very.program.this.like.i"
#Explanation: The words in the input string are reversed while maintaining the dots as separators, resulting in "much.very.program.this.like.i".
class Solution:
    def reverseWords(self, s):
        s = s[::-1]
        n = len(s)
        i = 0
        result = []
        l = 0
        while l < n:
            if s[l] != '.':
                if i != 0:
                    result.append('.')
                    i += 1
                # go to the end of the word
                r = l
                while r < n and s[r] != '.':
                    result.append(s[r])
                    i += 1
                    r += 1
                # reverse the word
                result[i - (r - l):i] = reversed(result[i - (r - l):i])
                l = r
            l += 1

        return ''.join(result)

#OR
class Solution:
    def reverseWords(self, s):
        # code here
        striped = s.strip(".")
        splited = striped.split(".")
        temp = -1
        reverse = []
        for i in range(len(splited)):
            if len(splited[temp]) is not 0:
                reverse.append(splited[temp])
            temp -= 1
            
        return ".".join(reverse)