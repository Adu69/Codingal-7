
#
# Activity 1 - ClimbStairs
# -
# WHAT YOU ARE BUILDING:
# A recursive function that counts every distinct path up a staircase
# when you can take 1 step or 2 steps at a time.
# ways(4) = 5 | ways(5) = 8 | ways(3) = 3
# -
# Task 1 - Define ways(stairs) with base case: if stairs ‹ 0: return 0
# Task 2 - Add second base case: if stairs == 0: return 1
# Task 3 - Add twoSteps = ways(stairs - 2) inside if stairs ›= 2:
# Task 4 - Add oneStep = ways (stairs - 1) and return twoSteps + oneStep
# Task 5 - Add input() and print() - test with n=4 (expect 5)


def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    twoSteps = ways(stairs - 2) if stairs >= 2 else 0
    oneStep = ways(stairs - 1)
    return twoSteps + oneStep

n = int(input("Enter the number of stairs: "))
print("Number of ways to climb:", ways(n))