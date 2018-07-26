import pygal

from dicing import Dicing

dice1 = Dicing()
dice2 = Dicing()

results1 = []
results2 = []
for roll_num in range(10000):
    results1.append(dice1.roll())
    results2.append(dice2.roll())

frequencies = [0] * (dice1.num_sides + dice2.num_sides)
for roll_num in range(10000):
    frequencies[results1[roll_num]+results2[roll_num]-1] += 1

hist = pygal.Bar()
hist.title = "Results of rolling two 6-side dice 10000 times"
hist.xvalue = [str(x) for x in range(2, dice1.num_sides + dice2.num_sides + 1)]
hist.x_title = "Dice Points"
hist.y_title = "Frequencies"

hist.add("D6", frequencies)
hist.render_to_file("dice_visual_2.svg")
