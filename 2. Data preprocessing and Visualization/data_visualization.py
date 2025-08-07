import matplotlib.pyplot as plt
import numpy as np

# Create random data
data = np.random.randn(1000)

# 1. Plot a histogram
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 2. Create a scatter plot
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red', edgecolor='black')
plt.title('Random Scatter Plot')
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.show()

# 3. Create a line chart
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)', color='green', linewidth=2)
plt.title('Line Chart of sin(x)')
plt.xlabel('X')
plt.ylabel('sin(x)')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

# 4. Create a bar chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 4]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='orange', edgecolor='black')
plt.title('Bar Chart of Categories')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()