import csv

import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
np.random.seed(1)

MostRetweet = '/Users/siyizhou/Documents/2020Fall/COMMresearch/data/mostRetweet.csv'

mrHeader = []
mrData = []
mrComment = []
mrRetweet = []
mrLikes = []

# reading csv file
with open(MostRetweet, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    mrHeader = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        mrData.append(row)

for row in mrData:
    mrComment.append(float(row[4]))
    mrRetweet.append(float(row[3]))
    mrLikes.append(float(row[5]))

X = np.atleast_2d(np.array(mrComment[:50])).T
print(X)

# Observations and noise
Y = np.array(mrRetweet[:50])
model = LinearRegression()
model.fit(X,Y)
model = LinearRegression().fit(X,Y)
r_sq = model.score(X,Y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
y_pred = model.predict(X)
#print('predicted response:', y_pred, sep='\n')
dy = 0.5 + 1.0 * np.random.random(Y.shape)

plt.figure()
plt.plot(X, Y, 'r:', label=r'$Original data point$')
plt.errorbar(X.ravel(), Y, dy, fmt='r.', markersize=10, label='Observations')
plt.plot(X, y_pred, 'b-', label='Prediction')
# plt.fill(np.concatenate([x, x[::-1]]),
#           np.concatenate([y_pred - 1.96 * sigma,
#                         (y_pred + 1.96 * sigma)[::-1]]),
#          alpha=.5, fc='b', ec='None', label='95% confidence interval')
plt.xlabel('$Number of Comment')
plt.ylabel('$Number of Retweet')
#plt.ylim(0, 20000)
#plt.xlim(0, 20000)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('/Users/siyizhou/Documents/2020Fall/COMMresearch/result/Comment_vs_retweet_all.png', dpi = 600)

###########################
##   LIKE vs RETWEET     ##
###########################

X = np.atleast_2d(np.array(mrLikes[:])).T
print(X)

# Observations and noise
Y = np.array(mrRetweet[:])
model = LinearRegression()
model.fit(X,Y)
model = LinearRegression().fit(X,Y)
r_sq = model.score(X,Y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
y_pred = model.predict(X)
#print('predicted response:', y_pred, sep='\n')
dy = 0.5 + 1.0 * np.random.random(Y.shape)

plt.figure()
plt.plot(X, Y, 'r:', label=r'$Original data point$')
plt.errorbar(X.ravel(), Y, dy, fmt='r.', markersize=10, label='Observations')
plt.plot(X, y_pred, 'b-', label='Prediction')
# plt.fill(np.concatenate([x, x[::-1]]),
#           np.concatenate([y_pred - 1.96 * sigma,
#                         (y_pred + 1.96 * sigma)[::-1]]),
#          alpha=.5, fc='b', ec='None', label='95% confidence interval')
plt.xlabel('$Number of Likes')
plt.ylabel('$Number of Retweet')
#plt.ylim(0, 20000)
#plt.xlim(0, 20000)
plt.legend(loc='upper left')
plt.tight_layout()

plt.savefig('/Users/siyizhou/Documents/2020Fall/COMMresearch/result/Comment_vs_Likes_all.png',dpi=600)


