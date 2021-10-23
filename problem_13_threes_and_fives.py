import problem_11_make_array
def threes_and_fives(an_array):
    count = 0 
    for i in an_array: # counting values that are divisble by 3 and 5
        if i%3 == 0 or i%5 == 0:
            count += 1

    arr = problem_11_make_array.make_array(0, count) # making an array with count
    arr_index = 0 # acessing arr 
    for index in range(0, len(an_array)): #iteraiting through the array again and adding values that are divisble by 3 and 5
        if an_array[index]%3 == 0 or an_array[index]%5 == 0:
            arr[arr_index] = an_array[index]
            arr_index += 1

    return arr #returning array with the values that are divisble

def main():
    print(threes_and_fives([0,1,2,3,4,5,6,7,8,9,10]))

main()