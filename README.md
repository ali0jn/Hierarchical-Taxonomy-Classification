# Hierarchical-Supervised-Learners
Accurately identifying organisms based on their partially available genetic material is an important task to explore the phylogenetic diversity in an environment. Specific fragments in the DNA sequence of a living organism have been defined as DNA barcodes and can be used as markers to identify species eficiently and efectively. The existing DNA barcode-based classification approaches suffer from three major issues: (i) most of them assume that the classification is done within a given taxonomic class and/or input sequences are pre-aligned, (ii) highly performing classifiers, such as SVM, cannot scale to large taxonomies due to high memory requirements, (iii) mutations and noise in input DNA sequences greatly reduce the taxonomic classification score. In order to address these issues, we propose a multi-level hierarchical classifier framework to automatically assign taxonomy labels to DNA sequences. We utilize an alignment-free approach called spectrum kernel method for feature extraction. We build a proof-of-concept hierarchical classifier with two levels, and evaluated it on real DNA sequence data from barcode of life data systems. We demonstrate that the proposed framework provides higher f1-score than regular classifiers. Besides, hierarchical framework scales better to large datasets enabling researchers to employ classifiers with high classification performance and high memory requirement on large datasets. Furthermore, we show that the proposed framework is more robust to mutations and noise in sequence data than the non-hierarchical classifiers.

#### Published by Journal of Bioinformatics and Computational Biology [(access full text)](https://doi.org/10.1142/S0219720020500262)

#### Contributors:
Ali Reza Ibrahimzada  
Huzeyfe Ayaz  
Gihad N. Sohsah  
Ali Cakmak
