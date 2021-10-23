import csv

def field_count(csv_filename):
    fields = 0 
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file) # parses through data, adds splits for you
        next(csv_file) # skips header line
        for row in csv_reader:
            fields += len(row) # for each row add the length of that row to add up all the fields in the file
 
    return fields

def main():
    print(field_count("grades_010.csv"))

main()