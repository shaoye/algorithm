class Solution:
    # matrix类型为二维列表，需要返回列表
    
    
    def printMatrix(self, matrix):
        ret = []
        while matrix:
            ret.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return ret
