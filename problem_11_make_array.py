def make_array(prototype, length):
    array = []
    for i in range(0, length):
        array.append(prototype)

    return array

def main():
    print(make_array(0, 5))

if __name__ == "__main__":
    main()