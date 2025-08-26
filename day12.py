def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:  # if it's a closing bracket
            top = stack.pop() if stack else '#'  # dummy if stack is empty
            if mapping[char] != top:
                return False
        else:
            stack.append(char)  # opening bracket
    
    return not stack  # valid if stack is empty
