def size_sort(array):

    '''
    The idea is to sort numbers within the difference
    between the size of the array and the current number.
    Complexity tends to O(n^2) in worst scenario and O(n) if
    already sorted.
    '''
    def difference(first, second):
        return second - first

    def sorting(array):
        try:
            sorted_array = list()
            size = len(array)
            min_diff = size
            for number in array:
                if difference(number, size) < min_diff:
                    sorted_array.append(number)
                    min_diff = difference(number, size)
            return sorted_array

        except (IndexError, TypeError):
            print("Given array is either empty or not an array")

        except (ValueError):
            print("Given array contain non numerical values")

    return sorting(array)

if __name__ == "__main__":
    example_array = list({1,4,3,2})
    print(size_sort(example_array))
