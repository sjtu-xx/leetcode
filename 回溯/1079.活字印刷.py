class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles_dict = {}
        for s in tiles:
            if s in tiles_dict:
                tiles_dict[s] += 1
            else:
                tiles_dict[s] = 1
    
    def count_tiles(self, tiles_dict):
        """
        直接计算添加一个元素的值，之后迭代计算加入n个元素的值
        """
        count = 0
        for k in tiles_dict.keys():
            if tiles_dict[k]>0:
                count += 1
                tiles_dict[k] -= 1
            else:
                continue
            count += self.count_tiles(tiles_dict)
            tiles_dict[k] += 1
        return count 
            
