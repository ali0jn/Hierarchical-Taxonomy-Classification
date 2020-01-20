import pickle
from sklearn.metrics import accuracy_score
import numpy as np

class MutationPredictions:

  def __init__(self):
    self.file_names = [f'mutation_acc_scores/mutation{i/10}.db' for i in range(1,11) if i != 2]
    self.classifiers = ['singlerf', 'hierarchicalrf', 'linearsvm']
    self.train_test = ['train', 'test']
    self.all_predictions = {}
    self.all_scores = {}

  def revise(self, key, pred):
    new_pred = {}
    for clf in self.classifiers:
      new_pred.setdefault(clf, {})
      for i in self.train_test:
        new_pred[clf].setdefault(i,[])
        for k in pred[key][clf][i]:
          y_true, y_pred = [], []
          for idx in range(len(k[0])):
            if isinstance(k[0][idx], np.ndarray):
              y_true.append(k[0][idx][0])
            else:
              y_true.append(k[0][idx])
            if isinstance(k[1][idx], np.ndarray):
              y_pred.append(k[1][idx][0])
            else:
              y_pred.append(k[1][idx])
          new_pred[clf][i].append((y_true, y_pred))
    return new_pred

  def acc_score(self):
    scores = {}
    for clf in self.classifiers:
      scores.setdefault(clf, {})
      for i in self.train_test:
        scores[clf].setdefault(i,[])
        for k in self.new_pred[clf][i]:
          scores[clf][i].append(accuracy_score(np.ravel(k[0]),np.ravel(k[1])))
    return scores

  def save_files(self):
    with open("all_mutation_predictions.db", 'wb') as file:
      pickle.dump(self.all_predictions, file)

    with open("all_mutation_accuracy_scores.db", 'wb') as file2:
      pickle.dump(self.all_scores, file2)

  def main(self):
    for file_name in self.file_names:
      with open(file_name, 'rb') as file:
        pred = pickle.load(file)
      keys = list(pred.keys())
      for key in keys:
        self.new_pred = self.revise(str(key), pred)
        self.all_predictions[str(key)] = self.new_pred
        self.all_scores[str(key)] = self.acc_score()
    self.save_files()

mt = MutationPredictions()
mt.main()