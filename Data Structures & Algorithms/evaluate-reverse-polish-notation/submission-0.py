class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l1=[]
        total=0
        for i in tokens:
            if i not in ["+","-","/","*"]:
                l1.append(int(i))
            else:
                operator=i
                num1=l1.pop()
                num2=l1.pop()
                if operator=="+":
                    total=num2+num1
                elif operator=="-":
                    total=num2-num1
                elif operator=="*":
                    total=num2*num1
                elif operator=="/":
                    total=int(float(num2)/num1)
                l1.append(total)
        return l1[-1]

        