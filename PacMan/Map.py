import csv


def result():
    results = []
    with open('testmaze.txt', newline='\n') as f:
        for row in csv.reader(f):
            results.append(row)
    return results
