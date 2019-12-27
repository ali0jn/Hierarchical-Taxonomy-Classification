def kmerize(file, k):
    features = {}
    feature_dictionaries = {}
    with open(file) as f:
        for line in f:
            feature_dict = {}
            tokens = line.split(',')
            seq = tokens[1].strip()[1:-1].strip()
            genus = tokens[2][1:-3].strip()

            # skip sequences with len < 657 (see p. 7 and ref [30] in the paper)
            if len(seq) < 657:
                continue

            for i in range(len(seq)-k):
                kmer = seq[i:i+k]
                feature_dict.setdefault(kmer, 0)
                feature_dict[kmer] += 1
                features.setdefault(kmer, True)
                
            feature_dictionaries[genus] = feature_dict

    feature_vectors = {}
    sorted_features = list(features.keys())
    sorted_features.sort()

    for genus in feature_dictionaries:
        feature_dict = feature_dictionaries[genus]
        feature_vector = []
        for feature in sorted_features:
            feature_vector.append(feature_dict.get(feature, 0))
        feature_vectors[genus] = feature_vector

    import json
    with open(str(k)+'kmerized' + '.' + file[0:file.index('.')] + '.json', 'w') as fp:
        json.dump(feature_vectors, fp)


files = ['Aves.csv']

for k in range(1, 8):
    for file in files:
        kmerize(file, k)
