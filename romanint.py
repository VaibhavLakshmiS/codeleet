class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
        result = 0  # final result 
        prev_val = 0 # prev val 
        curr_val = 0 # curr val
        for i in  range ( len(s)-1,-1,-1): # (reversing the string and then traversing thru it)
            curr_val=roman_dict[s[i]] # stores the last int value
            if curr_val<prev_val: # checks if the last int is less than the number before eg: IV I<V
                result-=curr_val # then we do 5 (V) - (I) 1 = (4) ( IV)  
            else:
                result+=curr_val # else add the values 
            prev_val=curr_val # change the prev val to the curr val 
        return result # return the resulting number from conv roman to int 
