from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import numpy as np

# max depth is the height of the tree, default None
# min impurity decrease : split nodes only if impurity decrease above threshold, default 0.0
classifier = DecisionTreeClassifier(max_depth=10, min_impurity_decrease=0.01)
x_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y_train = np.array([0, 1, 0])
classifier.fit(x_train, y_train)
x_test = [[6, 7, 8], [10, 21, 3], [3, 1, 7]]
y_predicted = classifier.predict(x_test)
print(y_predicted)

# data split
X = np.random.random((3, 4))
y = np.array([1, 2, 3])
X_train, Y_train, X_test, Y_test = train_test_split(X, y, test_size=0.2)
classifier.fit(X_train, Y_train)
Y_predicted = classifier.predict(X_train)
accuracy = accuracy_score(Y_test, Y_predicted)
p, r, f1, s = precision_recall_fscore_support(Y_test, Y_predicted)
conf_matrix = confusion_matrix(Y_test, Y_predicted)
print(conf_matrix)

# k-fold with 5 splits
kfold = KFold(n_splits=5, shuffle=True)
X = np.random.random((4, 5))
y = np.random.random(4)
for train_indices, test_indices in kfold.split(X, y):
    # executed 5 times, once per each k-fold iteration
    break

# cross-validation, this model does not shuffle data, you need to do it by manually
clf = DecisionTreeClassifier()
X = np.random.random((4, 5))
y = np.random.random(4)
acc = cross_val_score(clf, X, y, cv=5, scoring='accuracy')



