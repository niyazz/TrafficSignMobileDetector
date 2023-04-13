import csv

def count(srcName):

    """
    Counts classes input number.
    """
    classInputs = {}

    with open(srcName, 'rt') as initialFile:
        data = list(csv.reader(initialFile))
        for i in range(0, len(data)):
            row = data[i]
            imgClass = row[5]
            if imgClass in classInputs:
                classInputs[imgClass] += 1
            else:
                classInputs[imgClass] = 1
    
    print(dict(sorted(classInputs.items(), key=lambda item: item[0])))

count('classes.csv')