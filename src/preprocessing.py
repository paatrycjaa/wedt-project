import re
import numpy as np
import os
def clean_str(string):
    """
    string cleaning for dataset
    Every dataset is lower cased except
    """
    string = re.sub(r"\\", "", string)    
    string = re.sub(r"\'", "", string)    
    string = re.sub(r"\"", "", string)
    string = re.sub("\\n"," ", string)    
    return string.strip().lower()

def get_embeddings_index(PATH):
    ##get glove embeddings
    embeddings_index = {}
    f = open(os.path.join(os.getcwd(), PATH), encoding='utf8')
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
    f.close()
    return embeddings_index

def get_embeddings_matrix(word_index, EMBED_SIZE, embeddings_index):
        absent_words = 0
        embedding_matrix = np.zeros((len(word_index) + 1, EMBED_SIZE))

        for word, i in word_index.items():
                embedding_vector = embeddings_index.get(word)
                if embedding_vector is not None:
                        # words not found in embedding index will be all-zeros.
                    # if word_counts[word] > min_wordCount:
                    embedding_matrix[i] = embedding_vector
                else:
                    absent_words += 1
        print('Total absent words are', absent_words, 'which is', "%0.2f" % (absent_words * 100 / len(word_index)),
            '% of total words')
        return embedding_matrix
