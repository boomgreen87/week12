import csv
import matplotlib.pyplot as plt

categories = []
canada = []
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "CAN":
			canada.append([int(row[0]), row[5], row[6], row[7]]) # multidimensional array
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print('Total medals for Canada:', len(canada))
print('Total medals for the rest of the world:', len(world))

print('processed', line_count, 'rows of data')

gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in canada:
	if medal[0] == 1924 and medal[3] == "Gold":
		gold_1924.append(medal)
	elif medal[0] == 1948 and medal[3] == "Gold":
		gold_1948.append(medal)
	elif medal[0] == 1972 and medal[3] == "Gold":
		gold_1972.append(medal)
	elif medal[0] == 2002 and medal[3] == "Gold":
		gold_2002.append(medal)
	elif medal[0] == 2014 and medal[3] == "Gold":
		gold_2014.append(medal)

print('Canada won', len(gold_1924), 'gold medals in 1924.')
print('Canada won', len(gold_1948), 'gold medals in 1948.')
print('Canada won', len(gold_1972), 'gold medals in 1972.')
print('Canada won', len(gold_2002), 'gold medals in 2002.')
print('Canada won', len(gold_2014), 'gold medals in 2014.')

# Filter 2014 based on gender
# 
# Plot in a pie chart men vs women
# How many medals for each as a percentage of the total
men = []
women = []

for gender in gold_2014:
	if gender[1] == "Men":
		men.append(gender)
	elif gender[1] == "Women":
		women.append(gender)

print('Men won', len(men), 'gold medals in 2014.')
print('Women won', len(women), 'gold medals in 2014.')

menMedals = int(len(men) / len(gold_2014) * 100)
womenMedals = int(len(women) / len(gold_2014) * 100)

# Visualization
labels = "Men", "Women"
sizes = [menMedals, womenMedals]
colors = ['lightblue', 'pink']
explode = (0.2, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("How Many Gold Medals Did Canada Win In 2014? Men vs Women")
plt.xlabel("Gold medal counts in 2014")
plt.show()
