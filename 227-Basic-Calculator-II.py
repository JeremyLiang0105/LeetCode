class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if c == "+":
                    new = num1 + num2
                elif c == "-":
                    new = num2 - num1
                elif c == "*":
                    new = num1 * num2
                else:
                    new = int(num2 / num1)
                stack.append(new)
        return stack[0]
    
    # time complexity: O(n)
    # space complexity: O(n)
