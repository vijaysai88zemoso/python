from sys import argv

script, filename = argv

def check_the_file_type(filename):
    return filename.endswith('.csv')

def show_content(f):
    for line in f.readlines():
        starting_pos = 0
        char = ","
        occurence = 0
        for index, charecter in enumerate(line):
            if charecter == "\"" and occurence == 0:
                occurence = 1
                continue
            if charecter == "\"" and occurence == 1:
                occurence = 0
            if ((occurence == 0 and charecter == char) or index + 1 == len(line)):
                print str(line[starting_pos:index]),
                print "\t",
                starting_pos = index + 1
        print ""

if check_the_file_type(filename):
    target = open(filename, 'r')
    show_content(target)
    target.close()
else:
    print "Please pass the csv file as the arguent"
