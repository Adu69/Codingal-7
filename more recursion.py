
# Activity 2 - BalancedParentheses
# WHAT YOU ARE BUILDING:
"""A recursive function that generates every valid combination of n
 pairs of curly braces {. Rule 1: if l › r → place }
Rule 2: if 1 ‹ n → place {
n=2 gives 2, n=3 gives 5 results"""
#一
# Task 1 - Define paren(s, 1, r, P, n): if p == 2*n: print s and return
# Task 2 - Add the close-brace branch: if 1 › r: s[p] = "}" then recurse
# Task 3 - Add the open-brace branch: if 1 < n: s[p] = "(" then recurse
# Task 4 - Set up: s = [""] * 2 * n and call paren(s, 0, 0, 0, n)
# Task 5 - Test n=2 (expect {}{} and {{)}) then n=3 (expect 5 results)

def paren(s, l, r, p, n):
    if (p == 2*n):
        for ss in s:
            print(ss, end="")
        print("\n")
        return
    
    if (l>r):
        s[p] = "}"
        paren(s, l, r+1, p+1, n)

    if (l<n):
        s[p] = "{"
        paren(s, l+1, r, p+1, n)

#_____________________________________________________________________________

n = int(input("Enter the number of parentheses: "))
s = [""] * 2 * n
print("\n) ")
paren(s, 0, 0, 0, n)