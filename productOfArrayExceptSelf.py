class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #print "Nums is " + str(nums)
        multLeftToRight = self.retMultObj(nums)
        #print multLeftToRight
        multRightToLeft = self.retMultObj(nums[::-1])[::-1]
        #print multRightToLeft
        retValue = []
        for i in xrange(len(nums)):
            retValue.append(multLeftToRight[i]*multRightToLeft[i])
        return retValue
    
    def retMultObj(self, nums):
        retValue = [1]
        mult = 1
        for i in nums[:-1]:
            retValue.append(mult*i)
            mult *= i
        return retValue
def main():
    testObject = Solution()
    print testObject.productExceptSelf([1,2,3,4])
    
if __name__ == '__main__':
    main()          