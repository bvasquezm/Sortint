import random

def bogo_sort(array):

    '''
    Code source: https://python.algorithms-library.com/sorts/bogo_sort

    Messy sorting algorithm based on randomized arrays, also known as Stupid Sort
    and other names. The best and the worst algorithm there is.
    '''

    def is_sorted(array):
        try:
            prev_element = array[0]
            for element in array:
                if element < prev_element:
                    return False
                prev_element = element
            return True

        except (IndexError, TypeError):
            print("Given array is either empty or not an array")

    while not is_sorted(array):
        random.shuffle(array)
    return array

if __name__ == "__main__":
    example_array = list({1,4,3,2})
    print(bogo_sort(example_array))
