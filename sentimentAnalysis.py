import csv

import numpy as np
from matplotlib import pyplot as plt
#from sklearn.linear_model import LinearRegression
from polyglot.text import Text

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

polarity_sizes_by_words = [0,0,0,0]
polarity_sizes_by_senti = [0,0,0]
rlc3 = [0,0,0,
        0,0,0,
        0,0,0,]
rlc4 = [0,0,0,
        0,0,0,
        0,0,0,
        0,0,0,]

labels_polarity_by_words =["Neutral","Positive","Negative","Mixed"]
labels_polarity_by_senti =["Neutral","Positive","Negative"]
labels_rlc4 = ["Retweet","likes" ,"comment",
                               "Retweet","likes" ,"comment",
                               "Retweet","likes" ,"comment",
                               "Retweet","likes" ,"comment"]
labels_rlc3 = ["Retweet","likes" ,"comment",
                               "Retweet","likes" ,"comment",
                               "Retweet","likes" ,"comment"]
colorSenti = ["#EEC600", "#36AB00", "#EE3E00" ]
colorWords = ["#EEC600", "#36AB00", "#EE3E00","#6A6A6A"]

colorRLC3 = ["#BDFFED", "#BDE0FF", "#E0BDFF",
             "#BDFFED", "#BDE0FF", "#E0BDFF",
             "#BDFFED", "#BDE0FF", "#E0BDFF"]

colorRLC4 = ["#BDFFED", "#BDE0FF", "#E0BDFF",
             "#BDFFED", "#BDE0FF", "#E0BDFF",
             "#BDFFED", "#BDE0FF", "#E0BDFF",
             "#BDFFED", "#BDE0FF", "#E0BDFF",]

for i in range(493):
    if numNegWords[i]== 0 and numPosWords[i]== 0:
        polarity_sizes_by_words[0] += 1
        rlc4[0] += retweet[i]
        rlc4[1] += likes[i]
        rlc4[2] += comment[i]
    elif numPosWords[i] > abs(numNegWords[i]):
        polarity_sizes_by_words[1] += 1
        rlc4[3] += retweet[i]
        rlc4[4] += likes[i]
        rlc4[5] += comment[i]
    elif abs(numNegWords[i]) > numPosWords[i]:
        polarity_sizes_by_words[2] += 1
        rlc4[6] += retweet[i]
        rlc4[7] += likes[i]
        rlc4[8] += comment[i]
    elif numNegWords[i] < 0 and numPosWords[i] > 0 and numPosWords[i] == abs(numNegWords[i]):
        polarity_sizes_by_words[3] += 1
        rlc4[9] += retweet[i]
        rlc4[10] += likes[i]
        rlc4[11] += comment[i]
print(polarity_sizes_by_words)
print(rlc4)
totalNeutral = rlc4[0]+rlc4[1] + rlc4[2]
totalPos = rlc4[3]+rlc4[4] + rlc4[5]
totalNeg = rlc4[6]+rlc4[7] + rlc4[8]
totalMix = rlc4[9]+rlc4[10] + rlc4[11]
coeffNeutral = polarity_sizes_by_words[0]/ sum(polarity_sizes_by_words)
coeffPos = polarity_sizes_by_words[1]/ sum(polarity_sizes_by_words)
coeffNeg = polarity_sizes_by_words[2]/ sum(polarity_sizes_by_words)
coeffMix = polarity_sizes_by_words[3]/ sum(polarity_sizes_by_words)
for i in range(3):
    rlc4[i] = coeffNeutral * rlc4[i]/totalNeutral
    rlc4[i + 3] = coeffPos * rlc4[i + 3] / totalPos
    rlc4[i + 6] = coeffNeg * rlc4[i + 6] / totalNeg
    rlc4[i + 9] = coeffMix * rlc4[i + 9] / totalMix

for i in range(493):
    if senti_polarity_neg[i]== 0 and senti_polarity_pos[i]== 0:
        polarity_sizes_by_senti[0] += 1
        rlc3[0] += retweet[i]
        rlc3[1] += likes[i]
        rlc3[2] += comment[i]
    elif senti_polarity_pos[i] > abs(senti_polarity_neg[i]):
        polarity_sizes_by_senti[1] += 1
        rlc3[3] += retweet[i]
        rlc3[4] += likes[i]
        rlc3[5] += comment[i]
    elif abs(senti_polarity_neg[i]) > senti_polarity_pos[i]:
        polarity_sizes_by_senti[2] += 1
        rlc3[6] += retweet[i]
        rlc3[7] += likes[i]
        rlc3[8] += comment[i]
totalNeutral2 = rlc3[0]+rlc3[1] + rlc3[2]
totalPos2 = rlc3[3]+rlc3[4] + rlc3[5]
totalNeg2 = rlc3[6]+rlc3[7] + rlc3[8]
coeffNeutral2 = polarity_sizes_by_senti[0]/ sum(polarity_sizes_by_senti)
coeffPos2 = polarity_sizes_by_senti[1]/ sum(polarity_sizes_by_senti)
coeffNeg2 = polarity_sizes_by_senti[2]/ sum(polarity_sizes_by_senti)
for i in range(3):
    rlc3[i] = coeffNeutral2 * rlc3[i]/totalNeutral2
    rlc3[i + 3] = coeffPos2 * rlc3[i + 3] / totalPos2
    rlc3[i + 6] = coeffNeg2 * rlc3[i + 6] / totalNeg2

explode = (0.05,0.05,0.05,0.05)
explode2 = (0.05,0.05,0.05,
            0.05,0.05,0.05,
            0.05,0.05,0.05,
            0.05,0.05,0.05,)

# ow, ol,  op = plt.pie(polarity_sizes_by_senti, labels=labels_polarity_by_senti, colors=colorSenti,autopct= "%1.1f%%", pctdistance=0.9,startangle=90, frame=True)
# [t.set_fontsize(6) for t in op]
# w, l, p = plt.pie(rlc3, colors=colorRLC3, radius=0.75,autopct= "%1.1f%%",pctdistance=0.85,startangle=90)
# [t.set_rotation(315) for t in p]
# [t.set_fontsize(4) for t in p]
# centre_circle = plt.Circle((0, 0), 0.5, color='black', fc='white', linewidth=0)
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)
# # #
# plt.axis('equal')
# plt.title("Polarity by senti vs. retweet, likes,comment")
# plt.tight_layout()
# plt.savefig('/Users/siyizhou/Documents/2020Fall/COMMresearch/result/sentiment_polarity_by_senti_rlc.png' ,dpi = 600)


ow, ol, op = plt.pie(polarity_sizes_by_words, labels=labels_polarity_by_words, colors=colorWords,autopct= "%1.1f%%", pctdistance=0.85,startangle=90, frame=True)
[t.set_fontsize(6) for t in op]
#
w, l, p = plt.pie(rlc4, colors=colorRLC4, radius=0.75,autopct= "%1.1f%%", pctdistance=0.9,startangle=90)
[t.set_rotation(315) for t in p]
[t.set_fontsize(4) for t in p]
centre_circle = plt.Circle((0, 0), 0.5, color='black', fc='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# #
plt.axis('equal')
plt.title("Polarity by Words vs. retweet, likes,  comment")
plt.tight_layout()
plt.savefig('/Users/siyizhou/Documents/2020Fall/COMMresearch/result/sentiment_polarity_by_words_rlc.png' ,dpi = 600)
#
