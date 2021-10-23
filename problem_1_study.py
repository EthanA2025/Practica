def open_file(filename):
    print("Before opening file")
    file = open(filename)
    file.close()
    print("After opening file")

def main():
    open_file("test.txt")

main()

