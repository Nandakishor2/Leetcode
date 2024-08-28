class Solution(object):
    def intToRoman(self, num):
        roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    
        result = ""
        
        # Iterate through the Roman numeral list
        for value, symbol in roman_numerals:
            # Determine how many times the Roman numeral symbol can fit into the number
            while num >= value:
                result += symbol
                num -= value
                
        return result
        