import csv

Loiun = open('published_data/Loissant_raw.csv', 'r')
lo = list(csv.reader(Loiun))
a = []

for c in range(len(lo)):
    a.append( [[lo[c][0].split(';')[0], lo[c][1].split(';')[0]] for i in range(1)])

b = []
for i in a:
    b.append(i[0])

print(b)


with open('published_data/Loissant_raw_filter.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(['Gene symbol','UniProt'])
    for line in b:
        csvwriter.writerow(line)



    # break
Loiun.close()