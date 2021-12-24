class Solution:
    def isValid(self, s: str) -> bool:
        '''
         { [ (
         
         0 1 2 3 4 5
        "{ [ ] } ( )"
        
        - one condition must be even in length
        - 
        
        '''    
        
#         if len(s) %2 != 0:
#             return False
        
#                    # 0    1    2
#         open_br  = ['{', '[', '(']
#         close_br = ['}', ']', ')']
#         tracker = []
#         for char in s:
#             if char in open_br:
#                 tracker.append(char)
#             else:
#                 close_ind = close_br.index(char)
#                 if len(tracker) == 0:
#                     return False
#                 val = tracker.pop()
#                 open_ind = open_br.index(val)
#                 if close_ind != open_ind:
#                     return False
#         return len(tracker) == 0
        
        stack = []
        open_br  = ['{', '[', '(']
        close_br = ['}', ']', ')']
        for letter in s:
            if letter in open_br:
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                val = stack[len(stack) - 1]
                if open_br.index(val) == close_br.index(letter):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        