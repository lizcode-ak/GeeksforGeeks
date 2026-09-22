class Solution:
    def getPairs(self, arr):
        elements = set(arr)
        res = []
        for x in elements:
            if x < 0 and -x in elements:
                res.append([x, -x])
        if 0 in elements and arr.count(0) >= 2:
            res.append([0, 0])
        res.sort()
        return res
        
        
        
        
        
        
        
        
        '''n = len(arr)
        res = []
        for i in range(n):
            for j in range(i+1,n):
                if arr[i] + arr[j] == 0:
                    res.append([i,j])
        
        return res'''