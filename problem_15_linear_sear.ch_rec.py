def linear_search_rec(an_array, target, index=0): # set parameters for an_array a target value we are searching for and an index which defaults to 0
    if index > len(an_array): # If the index value is greater than the length of the array, i.e out of range than it cannot find and returns none
        return None
    elif an_array[index] == target: # when going through the array if the value at that index == target then return the index the value is found at. Ex: [1,2,3] is the array and target = 1 we will return 0 because the value at index 0 is 1.
        return index 
    else:
        return linear_search_rec(an_array, target, index + 1) # Otherwise if the value isn't equal increase index by 1 so we go through each index of the array and try to find if there is a value that is equal
    
def main():
    print(linear_search_rec([1,2,5,10,6], 10, 0))

main()