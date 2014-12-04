import numpy
import matplotlib.pyplot as plt
import csv

from sklearn import linear_model
from sklearn import datasets
from sklearn import svm
from sklearn.decomposition import PCA

featureMat = numpy.loadtxt('Data/DefendersFeatureMatrixMin.csv',delimiter = ",")
labels = numpy.loadtxt('Data/DefendersSalaryMin.csv',delimiter =",")
headers = numpy.loadtxt('Data/HeadersMin.csv', dtype = str , delimiter=",")

teams = ["Arsenal", "Aston Villa", "Blackburn Rovers", "Bolton Wanderers", "Chelsea", "Everton", "Fulham", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Norwich City", "Queens Park Rangers", "Stoke City", "Sunderland", "Swansea City", "Tottenham Hotspur", "West Bromwich Albion", "Wigan Athletic", "Wolverhampton Wanderers"]

# sentiment_file = open("Data/SoccerStats.csv", 'rU')
# reader = csv.reader(sentiment_file)
# index = 0
# for row in reader:
# 	if index == 0: 
# 		keys = row
# 		break


# reader = csv.DictReader(sentiment_file)
# sentiment_file.seek(0)

# goalsScoredAgainst = dict()

# with open('Data/DefendersAvg.csv', 'wb') as test_file:
# 	index = 0
# 	for row in reader:
# 		opposition = row['Opposition']
# 		if opposition in goalsScoredAgainst:
# 			goalsScoredAgainst[opposition] += int(row['Goals'])
# 		else:
# 			goalsScoredAgainst[opposition] = int(row['Goals'])
# labels = []
# for team in teams:
# 	if team != "Arsenal":
# 		labels.append(goalsScoredAgainst[team]*-1)
# 	labels.append(goalsScoredAgainst[team]*-1)
# 	labels.append(goalsScoredAgainst[team]*-1)
# 	labels.append(goalsScoredAgainst[team]*-1)



# pca = PCA(n_components = 2)
# featureMat = pca.fit(featureMat).transform(featureMat)

# plt.figure()
# for c,i,tname in zip("rgb", range(100), labels):
# 	plt.scatter(featureMat[labels == i, 0], featureMat[labels == i,1],c=c,label=tname)
# plt.legend()
# plt.show()

trainMat = featureMat[20:]
testMat = featureMat[:20]
trainLabels = labels[20:]
testLabels = labels[:20]

#model = linear_model.LinearRegression()
#model = linear_model.RidgeCV(alphas=[0.1, 1.0, 10])
#model = svm.SVR(kernel="linear")
#model = svm.SVR()
model = linear_model.BayesianRidge()
model.fit(trainMat,trainLabels)

predictions = model.predict(testMat)

fig = plt.figure()
ax = fig.add_subplot(111)

N = 20
ind = numpy.arange(N)
width = 0.4

# for index in range(len(predictions)):
# 	predictions[index] = predictions[index]*-1
# 	testLabels[index] = testLabels[index]*-1

rects1 = ax.bar(ind, predictions, width, color="red")
rects2 = ax.bar(ind+width, testLabels, width, color="yellow")
ax.set_title("Salary vs. Predicted")
ax.set_ylabel("Salary")
ax.set_xlabel("Player ID")
#ax.set_ylim(60,90)
ax.legend((rects1[0],rects2[0]), ("Predicted","Actual"))
plt.show()



# for index in range(len(predictions)):
# 	print str(testLabels[index])+": "+str(predictions[index])

norm = max(model.coef_.min()*-1,model.coef_.max())

for index in range(len(headers)):
 	print headers[index] +": "+str(model.coef_[index])

top5Indices = model.coef_.argsort()[-10:][::-1]
print "\n\n\n BEST 10"
for index in top5Indices:
	print headers[index] +": "+str(model.coef_[index]*100/norm)

top5Indices = model.coef_.argsort()[:10][::-1]
print "\n\n\n WORST 10"
for index in top5Indices:
	print headers[index] +": "+str(model.coef_[index]*100/norm)

