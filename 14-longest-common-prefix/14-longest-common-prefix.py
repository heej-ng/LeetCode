class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #strs = ["flower","flow","flight"]
        pre = strs[0]
        for i in range(1, len(strs)):
            common = ""
            minlen = len(pre)
            if minlen > len(strs[i]):
                minlen = len(strs[i])
                
            for j in range(minlen):
                if pre[j] != strs[i][j]:  # 다른 부분 시작
                    common = pre[0:j]
                    break
                    
                elif j == minlen-1:       # minlen 길이까지 같은 경우
                    common = pre[0:minlen]
            pre = common
        return pre
