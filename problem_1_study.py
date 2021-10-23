def open_file(filename):
    print("Before opening file") 
    file = open(filename) # open file
    file.close() # close that file
    print("After opening file")

def main():
    open_file("test.txt")

main()

