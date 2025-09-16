class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #the max prefix can be the entire first word.
        prefix = strs[0]

        if len(strs) == 0:
            return ""
        for i in range(1, len(strs)):
            #if the current prefix doesn't pass this current string
            while strs[i].find(prefix) != 0:
                #make it smaller until it does
                prefix = prefix[0: len(prefix) -1]
            if prefix == "":
                return ""
        return prefix