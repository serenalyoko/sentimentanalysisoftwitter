import csv

import numpy as np
from matplotlib import pyplot as plt


stats = '/Users/siyizhou/Documents/2020Fall/COMMresearch/data/stats.csv'

header = []
data = []
name = []
totalRetweet = []
totalReply = []
totalLikes = []
avgRetweet = []
avgReply = []
avgLikes = []

# reading csv file
with open(stats, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    header = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        data.append(row)

for row in data:
    name.append(row[0])
    totalRetweet.append(float(row[1]))
    totalReply.append(float(row[2]))
    totalLikes.append(float(row[3]))
    avgRetweet.append(float(row[4]))
    avgReply.append(float(row[5]))
    avgLikes.append(float(row[6]))

x = np.arange(5)
fig = plt.figure()
plt.bar(x, totalLikes, color ='#00A5E3' , alpha = 1,width = 0.25  ,label = 'totalLikes')
plt.bar(x, totalRetweet, color = '#FF828B', alpha = 1, width = 0.25, label = 'totalRetweet')
plt.bar(x, totalReply, color = '#FFBF65', alpha = 0.7, width = 0.25, label = 'totalComments' )
plt.legend(loc='upper right')
plt.xticks(x, name, color = 'grey', rotation=30, fontweight='bold', fontsize='9', horizontalalignment='right')

plt.tight_layout()
plt.savefig('/Users/siyizhou/Documents/2020Fall/COMMresearch/result/totalStats_stack.png' ,dpi = 600)


x = np.arange(5)
fig = plt.figure()
plt.bar(x, avgLikes, color ='#00A5E3' , alpha =1, width = 0.25, label = 'Average Likes')
plt.bar(x, avgRetweet, color = '#FF828B', alpha = 1, width = 0.25, label = 'Average Retweet')
plt.bar(x, avgReply, color = '#FFBF65', alpha = 0.7, width = 0.25, label = 'Average Comments' )
plt.legend(loc='upper right')
plt.xticks(x, name, color = 'grey', rotation=30, fontweight='bold', fontsize='9', horizontalalignment='right')

plt.tight_layout()
plt.savefig('/Users/siyizhou/Documents/2020Fall/COMMresearch/result/avgStats_stack.png' ,dpi = 600)

