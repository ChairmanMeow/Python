from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

print digits.data
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)

print clf.fit(digits.data[:-1], digits.target[:-1]) 
print clf.predict(digits.data[-1])