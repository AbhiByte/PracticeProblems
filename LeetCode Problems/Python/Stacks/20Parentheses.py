def isValid(s : str) -> bool:
        
    stack = []
    closeToOpen = {")" : "(", "}" : "{", "]" : "["}

    for char in s:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    
    if not stack:
        return True
    else:
        return False
