def stairways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return stairways(n - 1) + stairways(n - 2) + stairways(n - 3)
n = int(input("Enter the number of stairs: "))
ways = stairways(n)
print(f"There are {ways} ways to climb {n} stairs.")
def trace_stairways(n, path=None):
    if path is None:
        path = []
    if n < 0:
        return
    elif n == 0:
        print(path)
    else:
        trace_stairways(n - 1, path + [1])
        trace_stairways(n - 2, path + [2])
        trace_stairways(n - 3, path + [3])
n = int(input("Enter the number of stairs for tracing: "))
print(f"Tracing all ways to climb {n} stairs:")
trace_stairways(n)
def generate_braces(n, open_count=0, close_count=0, current=""):
    if len(current) == 2 * n:
        print(current)
        return
    if open_count < n:
        generate_braces(n, open_count + 1, close_count, current + "{")
    if close_count < open_count:
        generate_braces(n, open_count, close_count + 1, current + "}"
                        )
n = int(input("Enter the number of pairs of braces: "))
print(f"Generating all combinations of {n} pairs of braces:")
generate_braces(n)