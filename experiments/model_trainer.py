import numpy as np
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

def train_svms(name, taxonomies):
	linear_svm = SVC(gamma=1/taxonomies[name][0].shape[0],kernel="linear",probability=True,random_state=0)
	linear_svm.fit(taxonomies[name][0], taxonomies[name][1])
	return linear_svm

def return_predictions(idx, x, y_pred, y, model, X_train, X_test, predict_species):
    return predict_species(idx, x, y_pred, y, model, X_train, X_test)