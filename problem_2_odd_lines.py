def odd_lines(filename):
    with open(filename) as file:
        count = 1 # we start at line 1 in files so count = 1
        for line in file:
            stripped = line.strip() # For each file strip it of extra white space 
            if count%2 == 1: # if the line number % 2 == 1, this means it is odd so print that line
                print(stripped)
            count += 1 # increment count 

def main():
    odd_lines("test.txt")

main()