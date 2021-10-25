import numpy as np
from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
import graphviz
X = np.array([[0,1,1], [1,0,1], [1,1,1], [0,1,1], [0,0,1]])
y = np.array([1,0,1,1,0])
print(X)
print(y)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
X_test = np.array([[0,0,0], [1,1,0]])
y_test = np.array([0, 1])
predicted = clf.predict(X_test)
print(predicted)

dot_data = tree.export_graphviz(clf, filled=True, out_file=None)
print(dot_data)
graph = graphviz.Source(dot_data)
# print(graph)