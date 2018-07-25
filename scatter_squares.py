import matplotlib.pyplot as plt

input_values = list(range(1,1000 + 1))
squares = [x ** 2 for x in input_values]

plt.scatter(input_values, squares, c = squares, cmap = plt.cm.Blues, edgecolor = 'none', s = 40)

# Display the graph title and label the axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.axis([0, 1100, 0, 1100000])
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()
plt.savefig('./images/squares_scatter_plot.png')
