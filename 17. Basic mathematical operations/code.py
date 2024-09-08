def basic_op(operator, value1, value2):
    result = 0
    if operator == "+":
        result = value1 + value2
    elif operator == "-":
        result = value1 - value2
    elif operator == "*":
        result = value1 * value2
    else:
        result = value1 / value2
        
    return result