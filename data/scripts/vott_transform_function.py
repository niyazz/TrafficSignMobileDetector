import csv

def transform(srcName, dstName):

    """
    Transfor data to VoTT format with border coords caclulating.
    """

    with open(dstName,'w', newline='') as filteredFile:
        with open(srcName, 'rt') as initialFile:
            writer = csv.writer(filteredFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(['image','xmin','ymin','xmax','ymax','label'])

            data = list(csv.reader(initialFile))
            for i in range(0, len(data)):
                row = data[i]
                imgClass = row[5]
                imgName= row[0]
                writer.writerow([imgName, float(row[1]), float(row[2]), float(row[1])+float(row[3]), float(row[2])+float(row[4]), imgClass])

transform('filtered_additional.csv', 'vott_classes_additional.csv')