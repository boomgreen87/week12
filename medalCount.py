import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print('Stripping out categories')
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print('Gold')
				golds.append(row[7])
			elif row[7] == "Silver":
				print('Silver')
				silvers.append(row[7])
			elif row[7] == "Bronze":
				print('Bronze')
				bronzes.append(row[7])
			line_count += 1

print(len(golds), 'gold medals have been won since \'24')
print(len(silvers), 'silver medals have been won since \'24')
print(len(bronzes), 'bronze medals have been won since \'24')

totalMedals = len(golds) + len(silvers) + len(bronzes)

print('processed', line_count, 'lines of data. Total medals:', totalMedals)

# Find percentages of all medals
gold_percent = int(len(golds) / totalMedals * 100)
silver_percent = int(len(silvers) / totalMedals * 100)
bronze_percent = int(len(bronzes) / totalMedals * 100)

print(gold_percent, silver_percent, bronze_percent)

# Visualization
labels = "Gold", "Silver", "Bronze"
sizes = [gold_percent, silver_percent, bronze_percent]
colors = ['gold', 'silver', 'chocolate']
explode = (0.2, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("How Many Olympic Medals Have Been Won?")
plt.xlabel("Medals counts since 1924")
plt.show()

