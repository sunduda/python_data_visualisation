from dice import Dice
import pygal

# Create dices
nroll = 100000
dice_sides = [6, 8, 10, 16]
dices = [Dice(side) for side in dice_sides]
# Roll the dice several times and store the result in a array
results = []
for roll_num in range(nroll):
    result = 0
    for dice in dices:
        result = result + dice.roll()
    results.append(result)

# Analyse frequencies for each side occurrence
frequencies = [0] * (max(results) - min(results) + 1)
for value in range(min(results), max(results) + 1):
    frequency = results.count(value)
    frequencies[value-min(results)] = frequency

hist = pygal.Bar()
hist.add('Result of Rolling Dices', frequencies)
hist.title = 'Result of Rolling Dices'
hist.x_labels = list(range(min(results), max(results) + 1))
hist.x_title = 'Dice Side'
hist.y_title = 'Occurence'
hist.render_to_file('dice_visual.svg')