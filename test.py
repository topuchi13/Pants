import csv


COORDS = []
with open('city.csv', 'r')  as f:
    readcsv = csv.reader(f, delimiter = ',')
    for row in readcsv:
        COORDS.append((float(row[0]), float(row[1])))

for a in range(len(COORDS)):
    tempx0 = [x[0] for x in COORDS[a:a+1]]
    tempx1 = [x[1] for x in COORDS[a:a+1]]
    for b in range(len(COORDS)):
        tempy0 = [y[0] for y in COORDS[b:b+1]]
        tempy1 = [y[1] for y in COORDS[b:b+1]]
        if tempx0 == tempy0 and tempx1 == tempy1 :
            if a != b:
                print (COORDS[a:a+1])
                del COORDS[a:a+1]
