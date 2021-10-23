def threes_and_fives(an_array):
    arr = []
    for num in an_array:
        if num%3 == 0 or num%5 == 0:
            arr.append(num)
    
    return arr

def main():
    print(threes_and_fives([0,1,2,3,4,5,6,7,8,9,10]))

main()