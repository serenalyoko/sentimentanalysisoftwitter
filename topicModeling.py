import csv

import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from polyglot.text import Text
from sklearn.decomposition import LatentDirichletAllocation
import random
import pyLDAvis
import pyLDAvis.sklearn

MostRetweet = '/Users/siyizhou/Documents/2020Fall/COMMresearch/data/sentiment.csv'
header = []
data = []
comment = []
retweet = []
likes = []
content = []
numPosWords = []
numNegWords = []
senti_polarity_pos = []
senti_polarity_neg = []

# reading csv file
with open(MostRetweet, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    mrHeader = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        data.append(row)

#sentiments = [["name","content","number of positive words",
#               "number of negative words","positive sentiment", "Negative sentiment",
#               "comment","like","retweet","url"]]
for row in data:
    content.append((row[1]))
    numPosWords.append(float(row[2]))
    numNegWords.append(float(row[3]))
    senti_polarity_pos.append(float(row[4]))
    senti_polarity_neg.append(float(row[5]))
    comment.append(float(row[6]))
    likes.append(float(row[7]))
    retweet.append(float(row[8]))

count_vect = CountVectorizer(max_df = 0.8, min_df = 2, stop_words="english")
doc_term_matrix = count_vect.fit_transform(content)
LDA = LatentDirichletAllocation(n_components=5, random_state=42)
LDA.fit(doc_term_matrix)

# pyLDAvis.enable_notebook()
# pyLDAvis.sklearn.prepare(LDA, doc_term_matrix, count_vect, mds='tsne')

for i, topic in enumerate(LDA.components_):
    print("Top 10 words for topic#", i)
    print([count_vect.get_feature_names()[i] for i in topic.argsort()[-10:]])
    print("\n")