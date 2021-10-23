import arrays
import random

def random_array(size, min_value = 0, max_value = None):
    random.seed(0)

    #return None
    
    an_array = arrays.Array(size)

    if max_value == None:
        size == max_value
    
    for index in range(0,size):
        an_array[index] = random.randint(min_value, max_value)

    return an_array

def range_array(start, stop, step = 1):

    a_range = range(start, stop, step)

    length = len(a_range)
    an_array = arrays.Array(length, 0)

    for index in range(length):
        an_array[index] = a_range[index]
    
    return an_array

def test_random_array_10_0_10_seed_1():
    seed = random_array(10,0,0)
    assert seed == len(random_array(10,0,0))

def main():
    x = random_array(10,0,0)
    print(x)

    # random.seed(2)
    # x = random_array(10,0,100)
    # print(x)

if __name__ == "__main__":
    main()
