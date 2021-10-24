import array_utils
import csv
import arrays

# def parse(filename, a_character):
#     with open(filename) as csv_file:
#         csv_reader = csv.reader(csv_file)
#         arr = arrays.Array(len(csv_reader), "")
#         next(csv_file)
#         for line in csv_reader:
#             strip = line.strip()
#             for i in strip:
#                 if strip[i] == a_character:
#                     line[i] = arr[strip]

#     return arr

def filternames(filename, char):
    names = arrays.Array(20)
    i = 0
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            name = line[0]
            last = name.split()[1]
            last = last.lower()
            if char in last:
                name[i] = last
                i +=1
    return names

def factorials(n):
    if n <= 1:
        return 1
    else:
        return n * factorials(n-1)


# def palindrome(a_string):
#     a_string.lower() = a_string
#     a_string.strip() = a_string
#     if len(a_string) < 2:
#         return True
#     elif a_string[-1] == a_string[1]:
#         return palindrome(a_string[1])

#7
     

def main():
    print(factorials(0))
    # print(palindrome("racecar"))

main()