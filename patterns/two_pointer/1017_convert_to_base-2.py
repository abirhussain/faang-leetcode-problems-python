class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        stack = []
        binary_string = ""

        while n != 0:
            remainder = n % -2
            n = n // -2
            if remainder < 0:
                remainder += 2
                n += 1
            stack.append(str(remainder))

        while stack:
            binary_string += stack.pop()

        return binary_string