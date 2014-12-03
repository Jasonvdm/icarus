import csv
teams = ["Arsenal", "Aston Villa", "Blackburn Rovers", "Bolton Wanderers", "Chelsea", "Everton", "Fulham", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Norwich City", "Queens Park Rangers", "Stoke City", "Sunderland", "Swansea City", "Tottenham Hotspur", "West Bromwich Albion", "Wigan Athletic", "Wolverhampton Wanderers"]


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
labels = []
for team in teams:
	labels.append(goalsScoredAgainst[team])
	labels.append(goalsScoredAgainst[team])
	labels.append(goalsScoredAgainst[team])
	labels.append(goalsScoredAgainst[team])