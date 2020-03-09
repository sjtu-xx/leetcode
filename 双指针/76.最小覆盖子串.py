class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        def check_dic():
            for k,v in s_dict.items():
                if v < t_dict[k]:
                    return False
            return True
        
        def count_dic():
            return sum(s_dict.values())

        n = len(s)

        left = 0
        right = 0
        s_dict = {ch:0 for ch in t}
        if s[0] in s_dict.keys():
            s_dict[s[0]] = 1
        t_dict = {ch:0 for ch in t}
        
        for ch in t:
            t_dict[ch] +=1
        min_len = float("inf")
        min_s = ""
        while True:
            if check_dic():
                cur_len = right + 1 -left
                if cur_len<min_len:
                    min_len = cur_len
                    min_s = s[left:right+1]
                    if s[left] in s_dict.keys():
                        s_dict[s[left]] -= 1
                    left += 1
                else:
                    left +=1
                    if left > n-1:
                        break
                    if s[left-1] in s_dict.keys():
                        s_dict[s[left-1]] -=1
            else:
                right += 1
                if right > n-1:
                    break
                else:
                    if s[right] in s_dict.keys():
                        s_dict[s[right]]+=1
        return min_s

print(Solution().minWindow("ab","b"))
