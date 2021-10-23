def return_number_of_lines(filename):
    with open(filename) as file:
        count = 0
        for line in file: # for each line in the file add 1 to count
            count += 1 # increment count by 1 each time

    return count

def main():
    print(return_number_of_lines("test.txt"))

main()