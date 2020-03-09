class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        """
        分析题目，只需要确定前面两个数，之后的数就应当确定
        所以只要将前两个数进行分类，就可以
        """
        n = len(num)
        if n < 3:
            return False
        if num[0] == "000":
            return True
        for i in range(1, n-1):
            if num[0] == "0" and i > 1:
                continue
            # i为第一个字符串的长度
            for j in range(i+1, n):
                if num[i] == "0" and j-i>1:
                    continue
                num_list = [int(num[:i]),int(num[i:j])]
                tmp_num = num[j:]
                for _ in range(n//min(i,j-i)-1):
                    print(num_list,",",tmp_num)
                    if len(tmp_num) == 0:
                        return True
                    num3 = num_list[-2] + num_list[-1]
                    if tmp_num.startswith(str(num3)):
                        tmp_num = tmp_num[len(str(num3)):]
                        num_list.append(num3)
                        continue
                    else:
                        break
        return False
                
print(Solution().isAdditiveNumber("199111992"))
