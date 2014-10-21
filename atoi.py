import sys

class Solution:
    # @return an integer
    def atoi(self, str):
        ct = 0
        isNegative = False
        whitespace = [' ', '    ']
        answer = 0
        while str[ct] in whitespace:
            ct += 1
        if str[ct] == '-':
            isNegative = True
            ct += 1
        if str[ct] == '+':
            ct += 1
        try:
            for i in range(ct, len(str)):
                answer = (answer * 10) + int(str[ct])
        except:
            raise
            
        if isNegative:
            answer = answer * -1
            
        if answer > sys.maxsize:
            return sys.maxsize
        if answer < sys.minsize:
            return sys.minsize
        return answer
