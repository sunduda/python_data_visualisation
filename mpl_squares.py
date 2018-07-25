import matplotlib.pyplot as plt

input_values = list(range(1,5 + 1))
squares = [x ** 2 for x in input_values]

plt.plot(input_values, squares, linewidth = 5)

# Display the graph title and label the axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.tick_params(axis = 'both', labelsize = 14)


plt.show()
