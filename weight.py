#weight for the stuff
import csv
import re

words = dict()
score = 0.0
count = 0
total = 0

with open('info.csv', 'r+') as f:
    reader = csv.reader(f, delimiter=',')    
    
    for row in reader:
	score += float(row[0])
        for i in range(1,len(row)):
	    if row[i] not in words:
                words[row[i]] = 1
	    else:
                words[row[i]] += 1
            count += 1
        total += 1

ave = score/total
print len(words)


print len(words)

with open('info.csv', 'r+') as f:
    reader = csv.reader(f, delimiter=',')
    
    fi = open('matrix.csv', 'r+')
    writer = csv.writer(fi, delimiter=',')
    rows = []
    item = []
    item.append("score")

    for wo in words.keys():
        item.append(wo)

    rows.append(item)
    print(item)

    for row in reader:
        item = []
        item.append((float(row[0])-ave)/4.0)
        wordcount = 18
        for t in range(1, len(row)):
            if row[t] == words.keys()[0]:
                wordcount -= 1
        for i in range(1, len(words)):
            num = 0
            #print words.keys()[i]
            for x in range(1, len(row)):
                if row[x] == words.keys()[i]:
                   num += 1.0
            item.append(num)
        rows.append(item)
        print len(rows)
    
    writer.writerows(rows)
    
        
	
	
print total
print count
print score
print len(words)
		


