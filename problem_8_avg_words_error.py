def average_words(filename):
    lines = 0
    total_words = 0
    with open(filename) as file:
        for line in file:
            if line.strip() == "":
                    continue
            else:
                stripped = line.strip()
                words = line.split()
                total_words += len(words)
                lines += 1
    
    return total_words / lines

def main():
    print(average_words(".txt"))
    
main()