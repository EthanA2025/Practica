def even_letters(filename):
    with open(filename) as file:
        result = ""

        for line in file:
            line = line.strip() # strip the file so that we have no extra space

            for i in range(0, len(line)): # for each index in that certain line if that letters index is divisible by 2 add that index to our result
                if i % 2 == 0:
                    result += line[i]
    
    return result

def main():
    print(even_letters("alice.txt"))

main()