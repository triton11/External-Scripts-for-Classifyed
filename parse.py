import csv
import re

row = []
rows = []
with open('class.txt', 'r+') as f:
    group = re.findall("<option [^<]+ value=\"([^>]+)\">([^>]*)</option>", f.read())
    for i in group:
        rows.append(i)

 
with open('info.csv', 'r+') as fi:
   writer = csv.writer(fi, delimiter=',')
   writer.writerows(rows)
