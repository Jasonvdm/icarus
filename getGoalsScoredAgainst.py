import csv

sentiment_file = open("Data/SoccerStats.csv", 'rU')
reader = csv.reader(sentiment_file)
index = 0
for row in reader:
	if index == 0: 
		keys = row
		break
reader = csv.DictReader(sentiment_file)
sentiment_file.seek(0)

goalsScoredAgainst = []

with open('Data/DefendersAvg.csv', 'wb') as test_file:
	index = 0
	for row in reader:
		opposition = row['Opposition']
		if goalsScoredAgainst[opposition]:
			goalsScoredAgainst[opposition] += int(row['Goals'])
		else:
			goalsScoredAgainst[opposition] = int(row['Goals'])