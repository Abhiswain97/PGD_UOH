# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # **Implement TF-IDF from scratch**
#
# In this assignment, you will implement TF-IDF vectorization of text from scratch using only Python and inbuilt data structures. You will then verify the correctness of the your implementation using a "grader" function/cell (provided by us) which will match your implmentation.
#
# The grader fucntion would help you validate the correctness of your code.
#
# Please submit the final Colab notebook in the classroom ONLY after you have verified your code using the grader function/cell.
#
# **(FAQ) Why bother about implementing a function to compute TF-IDF when it is already available in major libraries?**
#
# Ans.
# 1. It helps you improve your coding proficiency.
# 2. It helps you obtain a deeper understanding of the concepts and how it works internally. Knowledge of the internals will also help you debug problems better.
# 3. A lot of product based startups and companies do focus on this in thier interviews to gauge your depth and clarity of understanding along with your programming skills. Hence, most top universities have implementations of some ML algorithms/concepts as mandatory assignments.
#
# **NOTE: DO NOT change the "grader" functions or code snippets written by us.Please add your code in the suggested locations.**
#
# Ethics Code:
# 1. You are welcome to read up online resources to implement the code.
# 2. You can also discuss with your classmates on the implmentation over Slack.
# 3. But, the code you wirte and submit should be yours ONLY. Your code will be compared against other stduents' code and online code snippets to check for plagiarism. If your code is found to be plagiarised, you will be awarded zero-marks for all assignments, which have a 10% wieghtage in the final marks for this course.

# %%
# Corpus to be used for this assignment

import numpy as np
import math
corpus = [
    'this is the first document mostly',
    'this document is the second document',
    'and this is the third one',
    'is this the first document here',
]


# %%
# Please implement this fucntion and write your code wherever asked. Do NOT change the code snippets provided by us.


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

# %% [markdown]
# # Grader Cell
# Please execute the following Grader cell to verify the correctness of your above implementation. This cell will print "Success" if your implmentation of the computeTFIDF() is correct, else, it will print "Failed". Make sure you get a "Success" before you submit the code in the classroom.


# %%
###########################################
# GRADER CELL: Do NOT Change this.
# This cell will print "Success" if your implmentation of the computeTFIDF() is correct.
# Else, it will print "Failed"
###########################################

# compute TF-IDF using the computeTFIDF() function
X_custom = computeTFIDF(corpus)

# Reference grader array - DO NOT MODIFY IT
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
