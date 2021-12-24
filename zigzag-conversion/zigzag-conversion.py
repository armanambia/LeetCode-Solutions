class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # type of res
        # key = rowNum
        # value = []
        res = {}
        
        if numRows == 1:
            return s 
        
        #  letter 5, and I have 4 rows
        #  0 1 2 3 4 5 6 7 8 9 10 11 12 13
        #  P A Y P A L I S H I R  I  N  G
        #  0 1 2 3 2 1 0 1 2 3 2  1  0  1
        #  numRows = 4
        counter = 0
        up = False
        
        
        for indx, letter in enumerate(s):
            
            
            
            if indx < numRows:
                res[indx] = [letter]
            else:
                res[counter].append(letter)
            
            
            temp = -1 if up else 1
            counter += temp
            
            if counter == numRows -1:
                up = True
            elif counter == 0:
                up = False
                                
        output = ''
        
        for value in res.values():
            output += ''.join(value)
            
        return output
        # add the lists together to concatenate the string