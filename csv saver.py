from sys import argv
from ast import literal_eval
import csv

script, filename = argv

list_of_tuples = literal_eval(raw_input("Enter list of tuples : "))

def writing_csv_file(list_of_tuples,filename):
    print "Opening the file..."
    target = open(filename, 'wt')

    print "Taking the input entered and converted to string and writing in csv file ..."
    try:
        writer = csv.writer(target)
        for tuples in list_of_tuples:
            writer.writerow(tuples)
    finally:
        target.close()
    print "Writing to csv is done"
    print "check the csv file"

writing_csv_file(list_of_tuples,filename)
