def odd_lines(filename):
    with open(filename) as file:
        count = 1
        for line in file:
            stripped = line.strip()
            if count%2 == 1:
                print(stripped)
            count += 1

def main():
    odd_lines("test.txt")

main()