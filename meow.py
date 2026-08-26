prices = [7, 1, 5, 3, 6, 4]

profit = 0

for i in range(1, len(prices)):
    jump = prices[i] - prices[i - 1]
    if jump > 0:
        profit += jump

print("Maximum Profit:", profit)

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

left_tallest = [0] * len(height)
right_tallest = [0] * len(height)

left_tallest[0] = height[0]

for i in range(1, len(height)):
    left_tallest[i] = max(left_tallest[i - 1], height[i])

right_tallest[-1] = height[-1]

for i in range(len(height) - 2, -1, -1):
    right_tallest[i] = max(right_tallest[i + 1], height[i])

water = 0

for i in range(len(height)):
    trapped = min(left_tallest[i], right_tallest[i]) - height[i]
    if trapped > 0:
        water += trapped

print("Trapped Rainwater:", water)