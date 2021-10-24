
def even_letters(filename):
    with open(filename) as file:
        result = ""

        for line in file:
            line = line.strip()

            for i in range(0, len(line)):
                if i % 2 == 0:

                    result += line[i]
    
    return result

def main():
    print(even_letters("alice.txt"))

main()