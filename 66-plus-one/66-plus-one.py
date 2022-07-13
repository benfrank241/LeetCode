class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry, x = 1,0
        
        while carry:
            if x < len(digits):
                if digits[x] == 9:
                    digits[x] = 0
                else:
                    digits[x] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            x += 1
        return digits[::-1]
            