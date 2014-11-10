import csv

sentiment_file = open("SoccerStats.csv", 'rU')
reader = csv.reader(sentiment_file)
index = 0
for row in reader:
	if index == 0: 
		keys = row
	index+=1
reader = csv.DictReader(sentiment_file)
sentiment_file.seek(0)
with open('Forwards.csv', 'wb') as test_file:
	index = 0;
	for row in reader:
		if index == 0: 
			file_writer = csv.DictWriter(test_file, keys)
			file_writer.writeheader()
		if row['Position Id'] == "6": file_writer.writerow(row)
		index +=1
test_file.close()