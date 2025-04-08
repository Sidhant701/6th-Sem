# from sklearn.model_selection import KFold
# kfold = KFold(n_splits=10, random_state=11, shuffle=True)

# from sklearn.model_selection import cross_val_score
# scores = cross_val_score(estimator=knn, X=dig.data, y=dig.target, cv=kfold)
# print(scores)

# print(f'Mean Accuracy: {scores.mean():.2%}')
# print(f'Accuracy Standard Deviation: {scores.std():.2%}')

# from sklearn.svm import SVC # svm: support vector mechanism, SVC: Support Vector Classifier
# from sklearn.naive_bayes import GaussianNB
# estimators = {'KNeighborsClassifier': knn, 'SupportVC': SVC(gamma = 'scale'), 'Gaussian Naive Bayes': GaussianNB()}
# for estimators_name, estimator_object in estimators.items():
#     kfold = KFold(n_splits=10, random_state=11, shuffle=True)
#     scores = cross_val_score(estimator=knn, X=dig.data, y=dig.target, cv=kfold)
#     print(f'{estimators_name:>20}: ' +
#           f'Mean Accuracy: {scores.mean():.2%}' +
#           f'Accuracy Standard Deviation: {scores.std():.2%}')
    

import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
c = lambda f: 5*((f-32)/9)
temps = [(f, c(f)) for f in range(0, 101, 10)]
# print(temps)

temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])
# print(temps_df)
# print(c(130))

plt.scatter(temps_df('Fahrenheit'), temps_df('Celsius'), marker='x', color='blue')
plt.xlabel('Fahrenheit (ind, x)')
plt.xlabel('Celsius (dep, y)')
plt.show()