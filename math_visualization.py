import numpy as np
import matplotlib.pyplot as plt

# =========================
# Task 1 - Function Visualization
# =========================

# Generate x values
x = np.linspace(-10, 10, 300)

# Define functions
y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

# Create figure
plt.figure(figsize=(10, 6))

# Plot functions
plt.plot(x, y1, label='y = x', linestyle='-')
plt.plot(x, y2, label='y = x^2', linestyle='--')
plt.plot(x, y3, label='y = sin(x)', linestyle='-.')
plt.plot(x, y4, label='y = e^(-0.1x) * cos(x)', linestyle=':')

# Labels and title
plt.title('Mathematical Function Visualization')
plt.xlabel('x')
plt.ylabel('y')

# Legend and grid
plt.legend()
plt.grid(True)

# Save figure
plt.savefig('function_plot.png')

# Show plot
plt.show()


# =========================
# Task 2 - Own Equation
# =========================

import numpy as np
import matplotlib.pyplot as plt

# =========================
# Task 1 - Function Visualization
# =========================

# Generate x values
x = np.linspace(-10, 10, 300)

# Define functions
y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

# Create figure
plt.figure(figsize=(10, 6))

# Plot functions
plt.plot(x, y1, label='y = x', linestyle='-')
plt.plot(x, y2, label='y = x^2', linestyle='--')
plt.plot(x, y3, label='y = sin(x)', linestyle='-.')
plt.plot(x, y4, label='y = e^(-0.1x) * cos(x)', linestyle=':')

# Labels and title
plt.title('Mathematical Function Visualization')
plt.xlabel('x')
plt.ylabel('y')

# Legend and grid
plt.legend()
plt.grid(True)

# Save figure
plt.savefig('function_plot.png')

# Show plot
plt.show()


# =========================
# Task 2 - Own Equation
# =========================

# Custom mixed equation:
# Combination of cubic and trigonometric behavior
y_custom = 0.02 * x**3 - 0.5 * x + 3 * np.sin(x)

plt.figure(figsize=(10, 6))

plt.plot(x, y_custom, label='Custom Equation')

plt.title('Custom Equation Visualization')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.savefig('own_equation.png')

plt.show()


# =========================
# Task 3 - Student Score Visualization
# =========================

students = ["S1", "S2", "S3", "S4", "S5",
            "S6", "S7", "S8", "S9", "S10"]

midterm = [85, 72, 90, 66, 78, 92, 60, 74, 88, 95]
final = [80, 70, 94, 68, 75, 90, 65, 72, 84, 96]

# Calculate total score
total = [0.4 * m + 0.6 * f for m, f in zip(midterm, final)]

# ---- A. Scatter Plot ----
plt.figure(figsize=(8, 6))

plt.scatter(midterm, final)

plt.title('Midterm vs Final Scores')
plt.xlabel('Midterm Score')
plt.ylabel('Final Score')
plt.grid(True)

plt.savefig('score_scatter.png')

plt.show()


# ---- B. Histogram ----
plt.figure(figsize=(8, 6))

plt.hist(total, bins=5)

plt.title('Distribution of Total Scores')
plt.xlabel('Total Score')
plt.ylabel('Frequency')
plt.grid(True)

plt.savefig('score_histogram.png')

plt.show()


# ---- C. Bar Chart ----
plt.figure(figsize=(10, 6))

plt.bar(students, total)

plt.title('Student Total Scores')
plt.xlabel('Students')
plt.ylabel('Total Score')
plt.grid(True)

plt.savefig('score_bar_chart.png')

plt.show()


# =========================
# Task 4 - Best-Fit Line
# =========================

# Linear regression
slope, intercept = np.polyfit(midterm, final, 1)

# Prediction line
predicted = slope * np.array(midterm) + intercept

plt.figure(figsize=(8, 6))

# Original data
plt.scatter(midterm, final, label='Original Data')

# Best-fit line
plt.plot(midterm, predicted, label='Best-Fit Line')

plt.title('Score Prediction using Best-Fit Line')
plt.xlabel('Midterm Score')
plt.ylabel('Final Score')

plt.legend()
plt.grid(True)

plt.savefig('score_prediction.png')

plt.show()

# Prediction examples
for score in [50, 75, 100]:
    predicted_score = slope * score + intercept
    print(f'Predicted final score for midterm {score}: {predicted_score:.2f}')