def open_file(filename):
    print("Before opening file")
    try:
        file = open(filename)
        file.close()
        print("After opening file")
    except FileNotFoundError:
        print("Error, file not found")

def main():
    open_file("ddsadasdsd.txt")

main()