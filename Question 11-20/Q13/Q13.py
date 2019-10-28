class Solution:
    def plusOne(self, digits):
        digits = digits[::-1]
        carry = 1

        for i in range(len(digits)):
            digits[i] += carry
            if(digits[i]<9):
                carry = 0
                break
            carry = digits[i]//10
            digits[i] -= 10

        if(carry>0):
            digits.append(carry)

        return digits[::-1]

print(Solution().plusOne([2,9,9]))