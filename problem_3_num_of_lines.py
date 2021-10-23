def return_number_of_lines(filename):
    with open(filename) as file:
        count = 0
        for line in file:
            count += 1

    return count

def main():
    print(return_number_of_lines("test.txt"))

main()