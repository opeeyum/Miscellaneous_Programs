"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""


def evalRPN(tokens) -> int:
    operator = ("+", "-", "*", "/")
    stack = []
    for token in tokens:
        if token not in operator:
            stack.append(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "-":
                stack.append(operand2 - operand1)
            elif token == "/":
                stack.append(int(operand2 / operand1))
    return stack.pop()


def func2():

    var1 = evalRPN(["2", "1", "+", "3", "*"])
    var2 = evalRPN(["4", "13", "5", "/", "+"])
    var3 = evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
    print(var1, var2, var3)


func2()
