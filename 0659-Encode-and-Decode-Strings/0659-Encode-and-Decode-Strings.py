class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        ans = ''
        for str in strs:
            if str == ":":
                ans = ans + str + ":"
            else:
                ans = ans + str
            ans = ans + ":;"

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        strs = []
        tempStr = ''
        for i in range(0, len(str)):
            if str[i] == ':' and str[i+1] == ";":
                strs.append(tempStr)
                tempStr = ''
            elif str[i] == ":":
                strs.append(":")
            elif str[i] == ";":
                continue
            else:
                tempStr = tempStr + str[i]
