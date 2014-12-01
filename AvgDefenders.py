import csv

sentiment_file = open("Data/StartingDefenders.csv", 'rU')
reader = csv.reader(sentiment_file)
index = 0
for row in reader:
	if index == 0: 
		keys = row
	index+=1
reader = csv.DictReader(sentiment_file)
sentiment_file.seek(0)
with open('Data/DefendersAvg.csv', 'wb') as test_file:
	index = 0
	lastIdNumber = 0
	numStarts = 0
	for row in reader:
		if index == 0: 
			file_writer = csv.DictWriter(test_file, keys)
			file_writer.writeheader()
			index+=1
			continue
		idNumber = row['Player ID']
		if idNumber == lastIdNumber:
			playerStats = dict( (n, playerStats.get(n, 0)+(float(row.get(n, 0)) if row.get(n,0).isdigit() else "")) for n in set(playerStats)|set(row) )
			numStarts +=1
		else:
			if index > 1:
				for key in playerStats:    
					if isinstance( playerStats[key], (int,long,float) ):
						playerStats[key] /=  numStarts
				file_writer.writerow(playerStats)
			playerStats = row
			for key in playerStats:    
				if playerStats[key].isdigit():
					playerStats[key] = float(playerStats[key])
			numStarts = 1
		index +=1
		lastIdNumber = idNumber
test_file.close()