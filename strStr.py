class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        h_len = len(haystack)
        n_len = len(needle)

        for i in range(0, 1 + h_len - n_len):
            if haystack[i:i+n_len] == needle:
                return i

        return -1

sol = Solution()
print (sol.strStr('hello', 'll'))
print (sol.strStr('hello', 'hell'))
print (sol.strStr('abdullah abu butata', 'bu'))
print (sol.strStr('snakes', ''))