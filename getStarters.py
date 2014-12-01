import csv

sentiment_file = open("Data/Defenders.csv", 'rU')
reader = csv.reader(sentiment_file)
index = 0
for row in reader:
	if index == 0: 
		keys = row
	index+=1
reader = csv.DictReader(sentiment_file)
sentiment_file.seek(0)
with open('Data/StartingDefenders.csv', 'wb') as test_file:
	index = 0;
	for row in reader:
		if index == 0: 
			file_writer = csv.DictWriter(test_file, keys)
			file_writer.writeheader()
		if row['Starter?'] == "1": file_writer.writerow(row)
		index +=1
test_file.close()