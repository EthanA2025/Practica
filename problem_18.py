import array_utils
import random

def SwapSort(an_array):
    print(an_array)
    for i in range(1, len(an_array)):
        if an_array[i] < an_array[i - 1]:
            swap = an_array[i]
            an_array[i] = an_array[i - 1]
            an_array[i - 1] = swap       
    
    return an_array

def main():
    
    arr = array_utils.random_array(10, 0, 10)
    print(SwapSort(arr))

if __name__ == "__main__":
    main()