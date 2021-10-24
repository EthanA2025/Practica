import problem_16
import array_utils
import random
import arrays

def rand_search(an_array, target):
    # check = arrays.Array(len(an_array))
    check = ""
    for i in range(0, len(an_array)):
        random_num = random.randint(0, len(an_array)-1) 
        while str(random_num) in check and len(check) <len(an_array): # If number is in the check until we find that index
            random_num = random.randint(0, len(an_array)-1)
        check += str(random_num)
        if an_array[random_num] == target:
            return random_num
        elif i == len(an_array):
            return None     
           

def main():
    arr = array_utils.random_array(20,0,20)
    print(arr)
    print(rand_search(arr, 1))
    
main()
