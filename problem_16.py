import problem_11_make_array
import array_utils
import arrays
import random

def shuffle(an_array):
    #random.seed(1)
    length = len(an_array)
    for _ in range(0, length): # iterate through a range of 0, to in this case 9.
        roll = random.randrange(0, length) # k is a random range from 0 to 9
        if roll == length: # If k is equal to length 
            length -= 1 # if this is true then decrement length
        else:
            swap = an_array[roll] # swapping algorithim, swap is equal to an_array[roll] ex:2
            an_array[roll] = an_array[length - 1] # example case: we roll a 2 so we swap 2 and the last index, 9. 
            an_array[length - 1] = swap # store swap
            length -= 1 # decrement

    return an_array

def main():
    print(shuffle([1,2,3,4,5,6,7,8,9,10]))

if __name__ == "__main__":
    main()