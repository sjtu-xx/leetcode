from typing import List

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        if n < 3:
            return []
        for i in range(1,len(S)-1):
            if S[0]=="0" and i>1:
                continue
            for j in range(i+1,len(S)):
                if S[i]=="0" and j-i>1:
                    continue
                Fibonacci_list = [int(S[:i]),int(S[i:j])]
                tmp_S = S[j:]
                while True:
                    if len(tmp_S) == 0:
                        return Fibonacci_list
                    num3 = sum(Fibonacci_list[-2:])
                    if num3 > 2**31 -1:
                        break
                    if tmp_S.startswith(str(num3)):
                        Fibonacci_list.append(num3)
                        tmp_S = tmp_S[len(str(num3)):]
                    else:
                        break
        return []

print("Solution",Solution().splitIntoFibonacci("417420815174208193484163452262453871040871393665402264706273658371675923077949581449611550452755"))
