import csv

def csvReader(csvFile):
    with open(csvFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='.')
        line_count = 0
        current_list = []
        for row in csv_reader:
            current_list.append(row[0])
            line_count += 1
    return current_list
        