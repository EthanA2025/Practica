import problem_11_make_array
import arrays
def string_to_array(a_string):
    array = problem_11_make_array.make_array("", len(a_string)) # make a blank array
    # print(array)
    for i in range(0, len(a_string)):
        array[i] = a_string[i] # for indexes in the range of 0 to the length of an array the array[i] = a_string[i]. Ex: at index 0, array[0] = "" and a-string[0] = "a" so then array[0] = "a". at index 1 array[1] = "" and a_string[1] = 'b' so now
                               # if we printed array we would have: ["a", "b"] and this continues for the len of that string
                             
    return arrays

def main():
    print(string_to_array("abcdefg"))

main()

