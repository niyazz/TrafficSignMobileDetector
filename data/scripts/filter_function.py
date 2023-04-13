import csv
import shutil

def filter():

    """
    Filter images from RTSD with certain classes.
    Creates new csv file, copies filtered images to destination.
    """
    initialRowAmount = 0
    filteredRowAmount = 0
    classes = {'1_8':0, '1_15':0, '1_16':0, '1_18':0, '1_20_2':0, '1_20_3':0, '1_21':0, '1_25':0, '3_11':0, '3_12':0, '3_13':0, '3_14':0, '1_19':0, '3_20':0, '3_21':0, '1_33':0, '2_6':0}

    with open('filtered_classes.csv','w', newline='') as filteredFile:
        with open('classes.csv', 'rt') as initialFile:
            data = list(csv.reader(initialFile))
            for i in range(1, len(data)):

                row = data[i]
                
                if len(row) <= 6:
                    continue

                initialRowAmount+=1
                imgClass = row[5]
                imgName= row[0]
                writer = csv.writer(filteredFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if imgClass in ['1_8', '1_15', '1_16', '1_18', '1_20_2', '1_20_3', '1_21', '1_25', '3_11', '3_12', '3_13', '3_14', '1_19', '3_20', '3_21', '1_33', '2_6']:
                    filteredRowAmount+=1
                    classes[imgClass] += 1
                    writer.writerow([imgName, row[1], row[2], row[3], row[4], imgClass])
                    shutil.copy2(f'./rtsd-frames/rtsd-frames/{imgName}', f'./rtsd-frames/filtered-frames/{imgName}')

    print(f'Initial images amount: {initialRowAmount}, filtered: {filteredRowAmount}')
    print("Represented classes:")
    print(classes)
        
filter()