import csv

def getCSVData(fileName):

    # Create an empty list to store rows
    rows = []

    #open the csv file
    dataFile = open(fileName, "r")

    # create a CSV Reader
    reader = csv.reader(dataFile)

    #skip header
    next(reader)

    #add rows from the file to the list
    for row in reader:
        rows.append(row)
    return rows