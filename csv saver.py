from sys import argv
from ast import literal_eval

script, filename = argv

list_of_tuples = literal_eval(raw_input("Enter list of tuples : "))

def writing_csv_file(list_of_tuples,filename):
    print "Opening the file..."
    target = open(filename, 'w')

    print "Truncating the file.  Goodbye!"
    target.truncate()

    print "Taking the input entered and converted to string and writing in csv file ..."
    for tuples in list_of_tuples:
        for index, s in enumerate(tuples):
            if "," in str(s):
                target.write("\"" + str(s) + "\"")
            else:
                target.write(str(s))
            if (index + 1) != len(tuples):
                target.write(",")
        target.write("\n")

    target.close();
    print "Writing to csv is done"
    print "check the csv file"
