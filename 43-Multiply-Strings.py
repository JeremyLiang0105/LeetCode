class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                res[i + j] += (digit % 10)
                res[i + j + 1] += (digit // 10)
    
        carry = 0
        for i in range(len(res)):
            tmp = res[i] + carry
            res[i] = (tmp) % 10
            carry = tmp // 10
        s = 0
        res = res[::-1]
        while s < len(res) and res[s] == 0:
            s += 1
        output = ""
        for n in res[s:]:
            output = output + str(n)
        return output
