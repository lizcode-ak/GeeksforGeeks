class Solution:
	def countOddEven(self, arr):
		ev = 0
		odd = 0
		for i in arr:
		    if i % 2 == 0:
		        ev += 1
            else:
                odd += 1
        return odd , ev
		