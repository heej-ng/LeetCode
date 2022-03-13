class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        max_cnt = 0
        cnt = 0
        # queue = ['0','1','2','3','4','5']
        # del queue[:cnt+1]
        # print(queue)
        
        for i in range(len(s)):
            
            if s[i] in queue:
                if cnt > max_cnt:
                    max_cnt = cnt
                
                for j in range(len(queue)):
                    if queue[j] == s[i]:
                        del queue[:j+1]
                        break
                        
                queue.append(s[i])
                cnt = len(queue)
                # if cnt > max_cnt:
                #     max_cnt = cnt
            else:
                queue.append(s[i])
                print(queue)
                cnt += 1
                
                
        if cnt > max_cnt:
            max_cnt = cnt
        return max_cnt
                
