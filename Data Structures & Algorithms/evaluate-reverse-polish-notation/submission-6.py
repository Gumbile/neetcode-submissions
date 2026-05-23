class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        check_list= ["+","-","/","*"]
        for x in tokens:
            if x not in check_list:
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.opertaion(x,a,b))
        return stack.pop()





    def opertaion(self,op,a,b) -> int:
        print(op,a,b)
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
           return int(a / b)
        else:
            return 0
        