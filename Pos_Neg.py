import csv

import numpy as np
from matplotlib import pyplot as plt
#from sklearn.linear_model import LinearRegression
from polyglot.text import Text


MostRetweet = '/Users/siyizhou/Documents/2020Fall/COMMresearch/data/mostRetweet.csv'
header = []
data = []
comment = []
retweet = []
likes = []
content = []
numPos = []
numNeg = []
polarity_pos = []
polarity_neg = []

# reading csv file
with open(MostRetweet, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    mrHeader = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        data.append(row)

for row in data:
    content.append(row[2])
    retweet.append(float(row[3]))
    comment.append(float(row[4]))
    likes.append(float(row[5]))

pos = set(line.strip() for line in open("positive-words.txt"))
neg = set(line.strip() for line in open('negative-words.txt'))

for j in range(len(content)):
    numPos.append(0)
    numNeg.append(0)
    polarity_pos.append(0)
    polarity_neg.append(0)

# text = Text("So ridiculous. Donald must work on his Anger Management problem, then go to a good old fashioned movie with a friend! Chill Donald, Chill!")
# print(text.sentences)
# print(text.entities)
# #e = text.entities
# # #
# for e in text.entities:
#     print("pos: ", e.positive_sentiment)
#     print("neg: ", e.negative_sentiment)

for i in range(len(content)):
    str = content[i]
    txt = Text(str)
    #print(str)
    for w in txt.words:
        if w.polarity > 0:
            polarity_pos[i] += 1
        if w.polarity < 0:
            polarity_neg[i] -= 1
    #print(txt.entities)
    for e in txt.entities:
        if polarity_pos[i] != 0:
            numPos[i] += e.positive_sentiment
        if polarity_neg[i] != 0:
            numNeg[i] -= e.negative_sentiment

sentiments = [["name","content","number of positive words",
               "number of negative words","positive sentiment", "Negative sentiment",
               "comment","like","retweet","url"]]
mixed = [["name","content","number of positive words",
          "number of negative words","positive sentiment", "Negative sentiment",
          "comment","like","retweet","url"]]
for i in range(493):
    tmp = [data[i][1], content[i], polarity_pos[i], polarity_neg[i],numPos[i], numNeg[i], comment[i], likes[i],retweet[i],data[i][6]]
    sentiments.append(tmp)
    if polarity_pos[i] == abs(polarity_neg[i]) and polarity_pos[i] != 0:
        mixed.append(tmp)

file = open('sentiment.csv', 'w+', newline='')
# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(sentiments)
file.close()

file2 = open('mixed.csv', 'w+', newline='')
# writing the data into the file
with file2:
    write = csv.writer(file2)
    write.writerows(mixed)
file.close()

sizes = [0,0,0,0]
for i in range(493):
    if polarity_neg[i]< 0 and polarity_pos[i]> 0 and polarity_pos[i] == abs(polarity_neg[i]):
        sizes[3] += 1
    elif polarity_neg[i]== 0 and polarity_pos[i]== 0:
         sizes[0] += 1
    elif abs(polarity_neg[i]) > polarity_pos[i]:
         sizes[2] += 1
    elif polarity_pos[i] > abs(polarity_neg[i]):
         sizes[1] += 1
# for i in range(493):
#     if numNeg[i]== 0 and numPos[i]== 0:
#         sizes[0] += 1
#     elif abs(numNeg[i]) > numPos[i]:
#         sizes[2] += 1
#     elif numPos[i] > abs(numNeg[i]):
#         sizes[1] += 1
labels = 'Neutral', 'Positive', 'Negative', "Mixed"
explode = (0, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
# #
fig1 = plt.figure()
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Polarity by words")
plt.tight_layout()
#
plt.savefig('/Users/siyizhou/Documents/2020Fall/COMMresearch/result/sentiment_polarity_by_words.png' ,dpi = 600)




