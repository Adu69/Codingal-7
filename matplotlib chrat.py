import matplotlib.pyplot as plt
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
scores = [70, 85, 60, 90, 75]
plt.plot(days, scores)
plt.show()

plt.plot(days, scores)
plt.title("My Daily Quiz Tracker")
plt.xlabel("Days of the Week")
plt.ylabel("Scores")
plt.grid(True)
plt.ylim(0, 100)
plt.show()

plt.plot(days, scores, color = 'green', marker='o', linestyle='dashed', linewidth = 2)
plt.title("My Daily Quiz Tracker")
plt.xlabel("Days of the Week")
plt.ylabel("Scores")
plt.grid(True)
plt.ylim(0, 100)
plt.show()

plt.bar(days, scores, color = 'orange')
plt.title("My Daily Quiz Tracker")
plt.xlabel("Days of the Week")
plt.ylabel("Scores")
plt.grid(False)
plt.ylim(0, 100)
plt.show()

plt.barh(days, scores, color = 'orange')
plt.title("My Daily Quiz Tracker")
plt.xlabel("Days of the Week")
plt.ylabel("Scores")
plt.grid(False)
plt.ylim(0, 100)
plt.show()