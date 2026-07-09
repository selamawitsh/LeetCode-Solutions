class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {")": "(", "}": "{", "]": "["}
        stack=[]

        for char in s:
            if char in valid_dict:
                if not stack:
                    return False
                top = stack.pop()
                if top != valid_dict[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0