#20. Valid Parentheses

# Note , in Python :
# list.append(value)    is the same as Stack.push(Value)
# x = list.pop()        is the same as x = Stack.pop()

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        m = {")": "(",     "]": "[",       "}": "{"}
        stack = []

        for x in s:
            print(f"x = {x} , stack before = {stack}")
            if x not in m:
                print(f"Pushed {x} to stack")
                stack.append(x)
                print(f"stack after Push = {stack}")
                print()
                continue

            print(f"m[x] = {m[x]} ")

            print(f"m[x]  == stack[-1] ?    {m[x]} == {stack[-1]} ?")
            if not stack or stack[-1]!= m[x]:
                print("No")
                return False

            print("Yes")

            y = stack.pop()
            print(f"popped {y}")
            print(f"stack after POP {stack}")
            print()
        return not stack



s = Solution()
sol = s.isValid("[")
print(sol)
