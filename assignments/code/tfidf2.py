import numpy as np
import math
corpus = [
    'this is the first document mostly',
    'this document is the second document',
    'and this is the third one',
    'is this the first document here',
]


def compute_tf(word, sen):
    count = 0
    for w in sen:
        if word == w:
            count += 1
    return count/len(sen)


def compute_idf(word):
    count = 0
    for doc in corpus:
        if word in doc:
            count += 1
    return math.log(len(corpus)/count)


def computeTFIDF(corpus):
    """Given a list of sentences as "corpus", return the TF-IDF vectors for all the 
    sentences in the corpus as a numpy 2D matrix. 

    Each row of the 2D matrix must correspond to one sentence 
    and each column corresponds to a word in the text corpus. 

    Please order the rows in the same order as the 
    sentences in the input "corpus". 

    Please order the words in the columns in the 
    alphabetic order when you featurize the corpus. 

    Ignore puncutation symbols like comma, fullstop, 
    exclamation, question-mark etc from the input corpus.

    For e.g, If the corpus contains sentences with these 
    9 distinct words, ['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this'], 
    then the first column of the 2D matrix will correpsond to word "and", the second column will 
    correspond to column "document" and so on. 

    Write this function using only basic Python code, inbuilt Data Structures and  NumPy ONLY.

    Implement the code as optimally as possible using the inbuilt data structures of Python.
    """

    ##############################################################
    ####   YOUR CODE BELOW  as per the above instructions #######
    ##############################################################
    word_list = list(map(lambda x: x.split(), corpus))

    tfidf = [[0] * len(word_list[0]) for _ in range(len(word_list))]

    for i in range(len(word_list)):
        for j in range(len(word_list[i])):
            tfidf[i][j] = round(compute_tf(
                word_list[i][j], word_list[i]) * compute_idf(word_list[i][j]), 2)

    return tfidf


X_custom = computeTFIDF(corpus)

X_grader = np.array(
    [[0, 0, 0, 0.12, 0.05, 0.23],
     [0, 0.1, 0, 0, 0.23, 0.1],
     [0.23, 0, 0, 0, 0.23, 0.23],
     [0, 0, 0, 0.12, 0.05, 0.23]]
)

# compare X_grader and X_custom
comparison = (X_grader == X_custom)
isEqual = comparison.all()

if isEqual:
    print("******** Success ********")
else:
    print("####### Failed #######")
    print("\nX_grader = \n\n", X_grader)
    print("\n", "*"*50)
    print("\nX_custom = \n\n", X_custom)


# %%
