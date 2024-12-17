class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for i in strs:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
        return prefix