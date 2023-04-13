import csv
import shutil

def filter(srcName, dstName, dstDirectory):

    """
    Filter images from RTSD with certain classes.
    Creates new csv file, copies filtered images to destination.
    """
    initialRowAmount = 0
    filteredRowAmount = 0
    classes = {'3_11':0, '3_12':0, '3_13':0, '3_14':0}

    with open(dstName,'w', newline='') as filteredFile:
        with open(srcName, 'rt') as initialFile:
            data = list(csv.reader(initialFile))
            for i in range(1, len(data)):

                row = data[i]
                
                if len(row) <= 6:
                    continue

                initialRowAmount+=1
                imgClass = row[5]
                imgName= row[0]
                writer = csv.writer(filteredFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                if imgClass in ['3_11_n13','3_11_n17', '3_11_n20','3_11_n23','3_11_n5','3_11_n8','3_11_n9','3_12_n10','3_12_n3','3_12_n5','3_12_n6','3_13_r2.5', '3_13_r3','3_13_r3.3','3_13_r3.5','3_13_r3.7','3_13_r3.9','3_13_r4','3_13_r4.1','3_13_r4.2','3_13_r4.3','3_13_r4.5','3_13_r5','3_13_r5.2','3_14_r2.7','3_14_r3','3_14_r3.5','3_14_r3.7']:
                    filteredRowAmount+=1
                    truncatedImgClass = imgClass[:4]
                    classes[truncatedImgClass] += 1
                    writer.writerow([imgName, row[1], row[2], row[3], row[4], truncatedImgClass])
                    shutil.copy2(f'./rtsd-frames/rtsd-frames/{imgName}', f'./rtsd-frames/{dstDirectory}/{imgName}')

    print(f'Initial images amount: {initialRowAmount}, filtered: {filteredRowAmount}')
    print("Represented classes:")
    print(classes)
        
filter("classes.csv", "filtered_additional.csv", "filtered-additional-frames")