def generateParenthesis(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack()
    return result

n = int(input("Enter the number of pairs of parentheses: "))
combinations = generateParenthesis(n)
print("All combinations of well-formed parentheses:")
for combo in combinations:
print(combo)
