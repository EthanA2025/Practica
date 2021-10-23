import arrays
import array_utils
def make_array(prototype, length):
    array = arrays.Array(length, prototype) # Use the arrays module and pass in our parameters to make an array
    return array

def main():
    print(make_array(0, 5)) # This will make an array of 5 zeros, 5 is length and 0 is the prototype (value)

if __name__ == "__main__":
    main()