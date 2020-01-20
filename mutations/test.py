import pickle

with open('all_mutation_accuracy_scores.db', 'rb') as my_file:
    out = pickle.load(my_file)
    print(out)