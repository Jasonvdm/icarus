import numpy
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn import datasets
from sklearn import svm
from sklearn.decomposition import PCA

featureMat = numpy.loadtxt('Data/DefendersFeatureMatrixMin.csv',delimiter = ",")
labels = numpy.loadtxt('Data/DefendersSalaryMin.csv',delimiter =",")
headers = numpy.loadtxt('Data/HeadersMin.csv', dtype = str , delimiter=",")

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

for index in range(len(predictions)):
	print str(testLabels[index])+": "+str(predictions[index])

for index in range(len(headers)):
 	print headers[index] +": "+str(model.coef_[index])


